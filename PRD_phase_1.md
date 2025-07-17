# Tax Advisor Application – Phase 1 PRD

## Phase 1: Project Setup, DB Schema, and Landing Page

---

### 1. Project Structure
- All code and configuration files must reside in the project root (not inside subfolders or the virtual environment).
- The following structure must be present:

```
.env
app.py
requirements.txt
supabase_db_create.py
/templates
    index.html
```
- No code, templates, or uploads inside the virtual environment directory (`tax_advisor/` is for venv only).
- The `/templates` folder is for HTML templates only.
- All secrets and credentials must be stored in `.env` at the root.

---

### 2. Landing Page
- A modern, branded landing page (`/templates/index.html`) with a clear "Start" button.
- Typography: Use "Aptos Display" font (or fallback sans-serif if unavailable).
- The landing page must be served by the backend (`app.py`) at the root.
- The landing page is the only user-facing page in this phase.

---

### 3. Database Schema: UserFinancials Table
- The following table must exist in Supabase (Cloud PostgreSQL):

| Column Name         | Data Type         | Description                        |
|--------------------|------------------|------------------------------------|
| session_id         | UUID             | Primary Key, unique session ID      |
| gross_salary       | NUMERIC(15, 2)   | Total gross salary                  |
| basic_salary       | NUMERIC(15, 2)   | Basic salary component              |
| hra_received       | NUMERIC(15, 2)   | HRA received                        |
| rent_paid          | NUMERIC(15, 2)   | Annual rent paid                    |
| deduction_80c      | NUMERIC(15, 2)   | 80C investments                     |
| deduction_80d      | NUMERIC(15, 2)   | 80D medical insurance               |
| standard_deduction | NUMERIC(15, 2)   | Standard deduction                  |
| professional_tax   | NUMERIC(15, 2)   | Professional tax paid               |
| tds                | NUMERIC(15, 2)   | Tax Deducted at Source              |
| created_at         | TIMESTAMPTZ      | Record creation timestamp           |

- The table must be created using the `DB_URL` from `.env` for all database operations.
- No other tables or schemas are required in this phase.

---

### 4. Integration Points
- `app.py` must serve `/templates/index.html` at the root URL (`/`).
- No other endpoints or user flows are required in this phase.
- The `UserFinancials` table must be created and accessible in Supabase.

---

### 5. Acceptance Criteria
- [ ] The project folder structure matches the specification above.
- [ ] `.env` exists at the root with `DB_URL` (and placeholder for `GEMINI_API_KEY`).
- [ ] `app.py` exists at the root and serves `/templates/index.html` at `/`.
- [ ] `/templates/index.html` is a modern, branded landing page with a "Start" button.
- [ ] The `UserFinancials` table exists in Supabase with the specified schema.
- [ ] No code, templates, or uploads are present inside the virtual environment directory.

---

### 6. Constraints & Notes
- All secrets and credentials must be stored in `.env` (never hardcoded).
- No persistent file storage or uploads in this phase.
- The virtual environment is for dependencies only.
- The application must be runnable with `python app.py` from the root.
- All dependencies must be listed in `requirements.txt`. 