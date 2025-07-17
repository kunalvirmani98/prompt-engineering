# Tax Advisor Application – Phase 5 PRD

## Phase 5: GitHub Repository Setup & Code Push

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

### 2. GitHub Repository Setup
- Create a new GitHub repository for the project (public or private as per team preference).
- Repository name should be clear and relevant (e.g., `tax-advisor-app`).
- Initialize the repository with a `main` branch.
- Add a project README.md with a brief description, setup instructions, and usage notes.

---

### 3. Version Control & Initial Commit
- Initialize git in the project root.
- Add all project files and folders (except those in `.gitignore`).
- Make an initial commit with a clear message (e.g., "Initial project structure and codebase").
- Push the commit to the GitHub repository on the `main` branch.

---

### 4. .gitignore Requirements
- A `.gitignore` file must be present at the project root.
- The following must be ignored:
  - Virtual environment directories (e.g., `tax_advisor/`, `venv/`)
  - `.env` (environment variables and secrets)
  - `/uploads` (temporary PDF storage)
  - `__pycache__/`, `*.pyc`, and other Python cache files
  - `ai_conversation_log.json` (if it contains user data)
- Example:
  ```
  tax_advisor/
  venv/
  __pycache__/
  *.pyc
  .env
  uploads/
  ai_conversation_log.json
  ```

---

### 5. Branching & Workflow
- Use the `main` branch for production-ready code.
- Feature branches may be used for new features or bug fixes, merged via pull requests.
- All code must be reviewed before merging to `main` (if team workflow allows).

---

### 6. Acceptance Criteria
- [ ] GitHub repository is created and accessible.
- [ ] All project files (except those in `.gitignore`) are committed and pushed to the `main` branch.
- [ ] `.gitignore` is present and correctly excludes sensitive and unnecessary files.
- [ ] README.md is present with project description and setup instructions.
- [ ] No code, templates, or uploads are present inside the virtual environment directory.
- [ ] All secrets and credentials are stored in `.env` (never committed to git).

---

### 7. Constraints & Notes
- The virtual environment is for dependencies only.
- The application must be runnable with `python app.py` from the root.
- All dependencies must be listed in `requirements.txt`.
- All database operations must use the `DB_URL` from `.env`. 