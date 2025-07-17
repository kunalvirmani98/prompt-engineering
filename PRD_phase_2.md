# Tax Advisor Application – Phase 2 PRD

## Phase 2: PDF Upload, Data Extraction, and Manual Data Review

---

### 1. Project Structure
- All code and configuration files must remain at the project root (not inside subfolders or the virtual environment).
- The following new/updated structure must be present:

```
.env
app.py
requirements.txt
supabase_db_create.py
/uploads
/templates
    index.html
    form.html
```
- `/uploads` is for temporary PDF storage (uploaded files are deleted after processing).
- `/templates/form.html` is the user data review/edit form.
- No code, templates, or uploads inside the virtual environment directory.

---

### 2. PDF Upload & Data Extraction
- User uploads a Pay Slip or Form 16 (PDF) via a form on the frontend.
- Allowed file type: PDF only. Reasonable file size limit (e.g., 5MB).
- Backend saves uploaded files to `/uploads`.
- Data is extracted from the PDF using:
  - `PyPDF2` for text extraction
  - `pytesseract` for OCR (if needed)
  - `Gemini` LLM for structuring and cleaning extracted data
- Extracted data is used to pre-fill the review form.
- Uploaded PDFs are deleted from `/uploads` after processing.

---

### 3. Manual Data Review & Regime Selection
- User is presented with a form (`/templates/form.html`) pre-filled with extracted data.
- User can review and edit all fields before submission.
- The form includes a radio button for selecting tax regime (Old/New).
- Fields to be included (at minimum):
  - Gross Salary
  - Basic Salary
  - HRA Received
  - Rent Paid
  - Deduction 80C
  - Deduction 80D
  - Standard Deduction
  - Professional Tax
  - TDS
  - Tax Regime (Old/New)

---

### 4. Backend Integration
- `app.py` must provide endpoints to:
  - Serve `/templates/form.html` for data review
  - Handle PDF upload and save to `/uploads`
  - Extract data and pre-fill the form
  - Handle form submission (save reviewed data for next phase)
- All file and data handling must use secure, session-based logic (UUIDs).
- All secrets and credentials must be stored in `.env` at the root.

---

### 5. Acceptance Criteria
- [ ] User can upload a PDF (Pay Slip or Form 16) via the web interface.
- [ ] Uploaded PDFs are saved to `/uploads` and deleted after processing.
- [ ] Data is extracted from the PDF using PyPDF2, pytesseract, and Gemini.
- [ ] User is presented with a form pre-filled with extracted data and can edit all fields.
- [ ] User can select their preferred tax regime (Old/New) via radio button.
- [ ] No code, templates, or uploads are present inside the virtual environment directory.
- [ ] All secrets and credentials are stored in `.env` (never hardcoded).

---

### 6. Constraints & Notes
- `/uploads` is for temporary storage only; files must be deleted after extraction.
- The virtual environment is for dependencies only.
- The application must be runnable with `python app.py` from the root.
- All dependencies must be listed in `requirements.txt`.
- All database operations must use the `DB_URL` from `.env`. 