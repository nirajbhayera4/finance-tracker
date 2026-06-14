import json
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse

from src.storage import load_expenses, save_expenses
from src.tracker import create_expense, get_summary


ROOT = Path(__file__).resolve().parent
PUBLIC_DIR = ROOT / "web"


class FinanceTrackerHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(PUBLIC_DIR), **kwargs)

    def do_GET(self):
        path = urlparse(self.path).path

        if path == "/api/expenses":
            expenses = load_expenses()
            self.send_json({
                "expenses": expenses,
                "summary": get_summary(expenses),
            })
            return

        if path == "/":
            self.path = "/index.html"

        return super().do_GET()

    def do_POST(self):
        path = urlparse(self.path).path

        if path != "/api/expenses":
            self.send_error(404, "Not found")
            return

        try:
            content_length = int(self.headers.get("Content-Length", "0"))
            payload = json.loads(self.rfile.read(content_length) or b"{}")
            expense = create_expense(payload.get("amount"), payload.get("category", ""))
        except (TypeError, ValueError, json.JSONDecodeError) as error:
            self.send_json({"error": str(error)}, status=400)
            return

        expenses = load_expenses()
        expenses.append(expense)
        save_expenses(expenses)

        self.send_json({
            "expense": expense,
            "expenses": expenses,
            "summary": get_summary(expenses),
        }, status=201)

    def send_json(self, payload, status=200):
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


def run(host="127.0.0.1", port=8000):
    server = ThreadingHTTPServer((host, port), FinanceTrackerHandler)
    print(f"Finance tracker frontend running at http://{host}:{port}")
    print("Press Ctrl+C to stop the server.")
    server.serve_forever()


if __name__ == "__main__":
    run()
