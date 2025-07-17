# Tax Advisor Application – Phase 6 PRD

## Phase 6: Render Integration & Environment Configuration

---

### 1. Project Structure
- All code and configuration files must reside in the project root (not inside subfolders or the virtual environment).
- The following structure must be present:

```
.env
app.py
requirements.txt
supabase_db_create.py
tax_calculator.py
ai_conversation_log.json
build.sh
/uploads
/templates
    index.html
    form.html
    results.html
    ask.html
    upload.html
```
- No code, templates, or uploads inside the virtual environment directory.

---

### 2. Render Web Service Setup
- Deploy the app as a **Render Web Service**.
- Connect the GitHub repository to Render.
- Enable auto-deploy on every push to the `main` branch.
- Use the default Render-provided HTTPS domain (no custom domain required).

---

### 3. Environment Variables
- Set the following environment variables in the Render dashboard (never commit secrets to git):
  - `GEMINI_API_KEY` (Google Gemini API key)
  - `DB_URL` (PostgreSQL connection string for Supabase)
- No additional environment variables are required unless new features are added.

---

### 4. System & Python Dependencies
- The deployment environment must have **Tesseract OCR** installed for PDF data extraction.
- All Python dependencies must be listed in `requirements.txt`.
- Use a `build.sh` script to automate system and Python dependency installation.

#### Example `build.sh`:
```sh
#!/usr/bin/env bash
set -o errexit
apt-get update && apt-get install -y tesseract-ocr
pip install -r requirements.txt
```

---

### 5. Build & Start Commands
- **Build Command:** `./build.sh`
- **Start Command:** `python app.py`

---

### 6. Acceptance Criteria
- [ ] The app is deployed as a Render Web Service and accessible via the Render-provided URL.
- [ ] Auto-deploy is enabled for every push to the `main` branch.
- [ ] All required environment variables are set in the Render dashboard.
- [ ] Tesseract OCR and all Python dependencies are installed via `build.sh`.
- [ ] The app runs with `python app.py` and is fully functional in production.
- [ ] No code, templates, or uploads are present inside the virtual environment directory.
- [ ] All secrets and credentials are stored in Render environment variables (never in git).

---

### 7. Constraints & Notes
- The virtual environment is for dependencies only.
- The application must be runnable with `python app.py` from the root.
- All dependencies must be listed in `requirements.txt`.
- All database operations must use the `DB_URL` from environment variables. 