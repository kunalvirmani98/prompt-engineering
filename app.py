import os
import uuid
from flask import Flask, render_template, request, redirect, url_for, session, send_from_directory, flash
from werkzeug.utils import secure_filename
from dotenv import load_dotenv
import PyPDF2
import pytesseract
from PIL import Image
import openai
import tempfile
import csv
from tax_calculator import compare_regimes
import json

# Load environment variables from .env
load_dotenv()

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf'}
SECRET_KEY = os.urandom(24)

app = Flask(__name__, template_folder='templates')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = SECRET_KEY

openai.api_key = os.getenv('GEMINI_API_KEY')

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            text += page.extract_text() or ""
    return text

def extract_text_with_ocr(pdf_path):
    try:
        from pdf2image import convert_from_path
    except ImportError:
        return ""
    images = convert_from_path(pdf_path)
    ocr_text = ""
    for img in images:
        ocr_text += pytesseract.image_to_string(img)
    return ocr_text

def structure_data_with_gemini(raw_text):
    # Placeholder for Gemini LLM call. Replace with actual API call.
    return {
        'gross_salary': 1200000,
        'basic_salary': 600000,
        'hra_received': 200000,
        'rent_paid': 180000,
        'deduction_80c': 150000,
        'deduction_80d': 25000,
        'standard_deduction': 50000,
        'professional_tax': 2500,
        'tds': 100000,
        'tax_regime': 'new',
    }

def save_to_csv(user_data, tax_data, session_id):
    user_financials_path = os.path.join('data', 'user_financials.csv')
    tax_comparison_path = os.path.join('data', 'tax_comparison.csv')
    # Write user financials
    user_fields = [
        'session_id', 'gross_salary', 'basic_salary', 'hra_received', 'rent_paid',
        'deduction_80c', 'deduction_80d', 'standard_deduction', 'professional_tax', 'tds'
    ]
    if not os.path.exists(user_financials_path):
        with open(user_financials_path, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=user_fields)
            writer.writeheader()
    with open(user_financials_path, 'a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=user_fields)
        row = {k: user_data.get(k, '') for k in user_fields}
        row['session_id'] = session_id
        writer.writerow(row)
    # Write tax comparison
    tax_fields = [
        'session_id', 'tax_old_regime', 'tax_new_regime', 'best_regime', 'selected_regime'
    ]
    if not os.path.exists(tax_comparison_path):
        with open(tax_comparison_path, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=tax_fields)
            writer.writeheader()
    with open(tax_comparison_path, 'a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=tax_fields)
        writer.writerow({
            'session_id': session_id,
            'tax_old_regime': tax_data['tax_old_regime'],
            'tax_new_regime': tax_data['tax_new_regime'],
            'best_regime': tax_data['best_regime'],
            'selected_regime': user_data['tax_regime'],
        })

def get_followup_question(user_data):
    # Placeholder: In production, generate a contextual question using Gemini API
    return "What are your main financial goals for the coming year? (e.g., saving for a house, retirement, children's education, etc.)"

def get_gemini_suggestions(user_data, user_answer):
    # Placeholder: In production, call Gemini API with user_data and user_answer
    # Return a list of actionable suggestions
    return [
        "Increase your 80C investments to maximize tax savings.",
        "Consider purchasing health insurance for additional 80D benefits.",
        "Invest in tax-saving mutual funds (ELSS) for higher returns.",
        f"Plan for your goal: {user_answer} with SIPs and PPF.",
    ]

def log_conversation(session_id, question, answer, suggestions):
    log_entry = {
        "session_id": session_id,
        "question": question,
        "answer": answer,
        "suggestions": suggestions
    }
    log_path = "ai_conversation_log.json"
    try:
        if not os.path.exists(log_path):
            with open(log_path, 'w') as f:
                json.dump([], f)
        with open(log_path, 'r+') as f:
            data = json.load(f)
            data.append(log_entry)
            f.seek(0)
            json.dump(data, f, indent=2)
            f.truncate()
    except Exception as e:
        print('Log error:', e)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        if 'pdf_file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['pdf_file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            session_id = str(uuid.uuid4())
            session['session_id'] = session_id
            save_path = os.path.join(app.config['UPLOAD_FOLDER'], f"{session_id}_{filename}")
            file.save(save_path)
            text = extract_text_from_pdf(save_path)
            if not text.strip():
                text = extract_text_with_ocr(save_path)
            extracted_data = structure_data_with_gemini(text)
            os.remove(save_path)
            session['extracted_data'] = extracted_data
            return redirect(url_for('review'))
        else:
            flash('Invalid file type. Please upload a PDF.')
            return redirect(request.url)
    return render_template('upload.html')

@app.route('/review', methods=['GET', 'POST'])
def review():
    if request.method == 'POST':
        reviewed_data = {
            'gross_salary': request.form.get('gross_salary'),
            'basic_salary': request.form.get('basic_salary'),
            'hra_received': request.form.get('hra_received'),
            'rent_paid': request.form.get('rent_paid'),
            'deduction_80c': request.form.get('deduction_80c'),
            'deduction_80d': request.form.get('deduction_80d'),
            'standard_deduction': request.form.get('standard_deduction'),
            'professional_tax': request.form.get('professional_tax'),
            'tds': request.form.get('tds'),
            'tax_regime': request.form.get('tax_regime'),
        }
        session['reviewed_data'] = reviewed_data
        session_id = session.get('session_id', str(uuid.uuid4()))
        # Tax calculation and CSV save
        tax_data = compare_regimes(reviewed_data)
        save_to_csv(reviewed_data, tax_data, session_id)
        # Pass all to results page, always show the AI advisor button
        return render_template('results.html',
            tax_old_regime=tax_data['tax_old_regime'],
            tax_new_regime=tax_data['tax_new_regime'],
            best_regime=tax_data['best_regime'],
            selected_regime=reviewed_data['tax_regime'],
            show_next=True
        )
    extracted_data = session.get('extracted_data', {})
    return render_template('form.html', **extracted_data)

@app.route('/ask', methods=['GET', 'POST'])
def ask():
    session_id = session.get('session_id', str(uuid.uuid4()))
    user_data = session.get('reviewed_data', {})
    followup_question = get_followup_question(user_data)
    ai_suggestions = None
    if request.method == 'POST':
        user_answer = request.form.get('user_answer')
        ai_suggestions = get_gemini_suggestions(user_data, user_answer)
        # Log conversation
        log_conversation(session_id, followup_question, user_answer, ai_suggestions)
        return render_template('ask.html', followup_question=followup_question, ai_suggestions=ai_suggestions)
    return render_template('ask.html', followup_question=followup_question, ai_suggestions=None)

@app.route('/restart', methods=['POST'])
def restart():
    session.clear()
    return redirect(url_for('index'))

@app.route('/upload.html')
def upload_html():
    return render_template('upload.html')

if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port) 