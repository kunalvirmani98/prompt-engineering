# Tax Advisor Application – Phase 3 PRD

## Phase 3: Tax Calculation Engine and Regime Comparison

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
/uploads
/templates
    index.html
    form.html
    results.html
```
- `/templates/results.html` is the results page for tax comparison.
- `tax_calculator.py` contains all tax calculation logic.
- No code, templates, or uploads inside the virtual environment directory.

---

### 2. Tax Calculation Logic
- Implement tax calculation for both Old and New regimes as per FY 2024-25 rules:
  - **Old Regime:**
    - Deductions: Standard Deduction (₹50k), HRA, Professional Tax, 80C, 80D, etc.
    - Slabs: 0% up to ₹2.5L, 5% up to ₹5L, 20% up to ₹10L, 30% above.
  - **New Regime (Default):**
    - Deductions: Standard Deduction (₹50k) only.
    - Slabs: 0% up to ₹3L, 5% up to ₹6L, 10% up to ₹9L, 15% up to ₹12L, 20% up to ₹15L, 30% above.
  - 4% cess applies to the final tax amount in both regimes.
- All calculation logic must be in `tax_calculator.py`.

---

### 3. Results Display & Comparison
- After calculation, show results in `/templates/results.html`:
  - Two visually distinct cards: one for Old Regime, one for New Regime.
  - Highlight the user’s selected regime.
  - Show calculated tax for both regimes, and which regime is better (lower tax).
- The results page is rendered by the backend; frontend only handles form submission and result display.

---

### 4. Database Integration
- Save all user financial data and tax results to Supabase:
  - `UserFinancials` table: Save all reviewed/entered data with session ID.
  - `TaxComparison` table: Save calculated tax for both regimes, best regime, selected regime, and session ID.
- All database operations must use the `DB_URL` from `.env`.

---

### 5. Backend Integration
- `app.py` must provide endpoints to:
  - Process reviewed data and call `tax_calculator.py` for calculations.
  - Render `/templates/results.html` with the comparison results.
  - Save all relevant data to the database.

---

### 6. Acceptance Criteria
- [ ] User sees a results page with two cards comparing Old and New Regime tax.
- [ ] The user’s selected regime is visually highlighted.
- [ ] Calculated tax for both regimes is shown, with the better regime indicated.
- [ ] All user data and tax results are saved to the database (`UserFinancials` and `TaxComparison`).
- [ ] No code, templates, or uploads are present inside the virtual environment directory.
- [ ] All secrets and credentials are stored in `.env` (never hardcoded).

---

### 7. Constraints & Notes
- The virtual environment is for dependencies only.
- The application must be runnable with `python app.py` from the root.
- All dependencies must be listed in `requirements.txt`.
- All database operations must use the `DB_URL` from `.env`. 