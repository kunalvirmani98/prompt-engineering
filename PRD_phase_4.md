# Tax Advisor Application – Phase 4 PRD

## Phase 4: Gemini-powered Advisor (Q&A, Suggestions)

---

### 1. Project Structure
- All code and configuration files must remain at the project root (not inside subfolders or the virtual environment).
- The following new/updated structure must be present:

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
```
- `/templates/ask.html` is the page for AI-powered Q&A and suggestions.
- `ai_conversation_log.json` stores the full conversation history for each session.
- No code, templates, or uploads inside the virtual environment directory.

---

### 2. Gemini-powered Advisor Flow
- After tax results, Gemini proactively asks a smart, contextual follow-up question based on the user's data.
- User answers the question via a form on `/templates/ask.html`.
- Gemini provides personalized, actionable investment and tax-saving suggestions in a modern, readable card format.
- The full conversation (questions, answers, suggestions) is logged in `ai_conversation_log.json` with the session ID.

---

### 3. Backend Integration
- `app.py` (or a helper) must provide endpoints to:
  - Serve `/templates/ask.html` for the Q&A flow.
  - Generate and display Gemini's follow-up question after tax results.
  - Accept and process the user's answer.
  - Call Gemini API to generate personalized suggestions.
  - Render suggestions in `/templates/ask.html`.
  - Log the full conversation to `ai_conversation_log.json` (append per session).
- All secrets and credentials must be stored in `.env` at the root.

---

### 4. Results Display
- Suggestions must be shown in a modern, readable card format on `/templates/ask.html`.
- The page should be visually appealing, accessible, and match the app's overall design.

---

### 5. Acceptance Criteria
- [ ] After tax results, user receives a relevant follow-up question from Gemini.
- [ ] User can answer the question and receive personalized, actionable suggestions.
- [ ] Suggestions are displayed in a modern, readable card format.
- [ ] The full conversation is logged in `ai_conversation_log.json` with the session ID.
- [ ] No code, templates, or uploads are present inside the virtual environment directory.
- [ ] All secrets and credentials are stored in `.env` (never hardcoded).

---

### 6. Constraints & Notes
- The virtual environment is for dependencies only.
- The application must be runnable with `python app.py` from the root.
- All dependencies must be listed in `requirements.txt`.
- All database operations must use the `DB_URL` from `.env`. 