# Finance Tracker

A simple personal finance tracker built with Python. The project keeps expenses in a plain text file and supports two ways to use the same data:

- A command-line interface from `main.py`
- A web frontend with GSAP animations from `web_app.py`

## About the Project

Finance Tracker lets you add expenses, group them by category, and view total spending. The Python storage layer saves data to `data/expenses.txt`, so both the CLI and frontend read from and write to the same file.

Each expense is stored as:

```text
amount,category
```

Example:

```text
12.50,Food
45.00,Transport
```

## Requirements

- Python 3.10 or newer
- A modern web browser
- Internet access for GSAP CDN animations in the frontend

## Dependencies

This project does not require any installed Python packages. It uses only Python standard library modules:

- `http.server`
- `json`
- `pathlib`
- `urllib.parse`
- `os`

Frontend dependency:

- GSAP 3, loaded from CDN in `web/index.html`

## Project Structure

```text
finance-tracker/
+-- data/
|   +-- expenses.txt
+-- src/
|   +-- __init__.py
|   +-- storage.py
|   +-- tracker.py
+-- web/
|   +-- app.js
|   +-- index.html
|   +-- styles.css
+-- main.py
+-- web_app.py
+-- README.md
```

## Run the CLI

```powershell
python main.py
```

CLI options:

1. Add expense
2. Show summary
3. Save and exit

## Run the Web Frontend

```powershell
python web_app.py
```

Then open:

```text
http://127.0.0.1:8000
```

The web frontend provides:

- Expense entry form
- Total spending summary
- Expense count
- Category totals
- GSAP page and list animations

## API Endpoints

### Get expenses

```http
GET /api/expenses
```

Returns all saved expenses and summary data.

### Add expense

```http
POST /api/expenses
Content-Type: application/json
```

Example body:

```json
{
  "amount": 12.5,
  "category": "Food"
}
```

## Notes

- The CLI behavior is preserved.
- The frontend uses the same Python storage functionality as the CLI.
- Expense data is saved locally in `data/expenses.txt`.
