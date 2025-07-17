# Tax Advisor Application

A web-based platform for salaried individuals in India to analyze tax liabilities, compare regimes, and receive personalized, AI-powered tax-saving strategies.

## Features
- Upload Pay Slip or Form 16 (PDF)
- Auto-extract and review salary data
- Tax calculation and regime comparison (Old vs. New)
- AI-powered advisor for personalized suggestions (Gemini LLM)
- Data saved securely to Supabase

## Project Structure
```
.env
app.py
requirements.txt
supabase_db_create.py
tax_calculator.py
ai_conversation_log.json
/uploads
/templates
    index.html
    form.html
    results.html
    ask.html
    upload.html
```

## Setup Instructions
1. Clone the repository:
   ```sh
   git clone <your-repo-url>
   cd <repo-folder>
   ```
2. Create and activate a Python virtual environment (recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Create a `.env` file in the root with your credentials:
   ```env
   GEMINI_API_KEY=<your-gemini-api-key>
   DB_URL=postgresql://postgres:<password>@<host>:5432/postgres
   ```
5. Run the database setup script:
   ```sh
   python supabase_db_create.py
   ```
6. Start the application:
   ```sh
   python app.py
   ```

## Usage Notes
- All secrets and credentials must be stored in `.env` (never committed to git).
- The `/uploads` folder is for temporary PDF storage and is ignored by git.
- The application is production-ready for deployment on Render or similar platforms.

## License
MIT 