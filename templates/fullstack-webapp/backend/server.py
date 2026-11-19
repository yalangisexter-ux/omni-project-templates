"""
TaskPulse Pro - Full-Stack REST API & Web Application Server
-----------------------------------------------------------
Pure Python Standard Library (0 external pip dependencies) + SQLite3 database.
Drop-in full-stack microservice ready for Docker, Linux, macOS, and Windows.
"""

import json
import sqlite3
import sys
from http.server import HTTPServer, BaseHTTPRequestHandler
from pathlib import Path
from urllib.parse import urlparse, parse_qs

BASE_DIR = Path(__file__).resolve().parent
DB_FILE = BASE_DIR / "taskpulse.db"
STATIC_DIR = BASE_DIR / "static"
STATIC_DIR.mkdir(parents=True, exist_ok=True)


def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            status TEXT DEFAULT 'todo',
            priority TEXT DEFAULT 'medium',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    # Seed sample tasks if table is empty
    c.execute("SELECT COUNT(*) FROM tasks")
    if c.fetchone()[0] == 0:
        seed_data = [
            ("Deploy QLoRA Model to Hugging Face", "Autonomous build and benchmark verification", "completed", "high"),
            ("Build Production GGUF Quantizations", "Generate Q4_K_M, Q5_K_M, Q8_0 binaries", "completed", "high"),
            ("Configure Client Requirements Test Suite", "Rigorous QA checks for 100% customer compliance", "in_progress", "medium"),
            ("Publish Fiverr Multi-Vertical Gigs", "Setup Logo, Web App, and APK listings", "todo", "low")
        ]
        c.executemany("INSERT INTO tasks (title, description, status, priority) VALUES (?, ?, ?, ?)", seed_data)
        conn.commit()
    conn.close()


class TaskPulseHandler(BaseHTTPRequestHandler):
    def _send_json(self, data, status=200):
        body = json.dumps(data, indent=2).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()
        self.wfile.write(body)

    def do_OPTIONS(self):
        self._send_json({"status": "ok"})

    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path
        query = parse_qs(parsed.query)

        if path == "/health":
            self._send_json({"status": "HEALTHY", "version": "1.0.0", "service": "TaskPulse Pro API"})
            return

        if path == "/api/tasks":
            conn = sqlite3.connect(DB_FILE)
            c = conn.cursor()
            status_filter = query.get("status", [None])[0]
            if status_filter:
                c.execute("SELECT id, title, description, status, priority, created_at FROM tasks WHERE status = ? ORDER BY id DESC", (status_filter,))
            else:
                c.execute("SELECT id, title, description, status, priority, created_at FROM tasks ORDER BY id DESC")
            rows = c.fetchall()
            conn.close()
            tasks = [
                {"id": r[0], "title": r[1], "description": r[2], "status": r[3], "priority": r[4], "created_at": r[5]}
                for r in rows
            ]
            self._send_json({"tasks": tasks, "count": len(tasks)})
            return

        if path == "/api/stats":
            conn = sqlite3.connect(DB_FILE)
            c = conn.cursor()
            c.execute("SELECT status, COUNT(*) FROM tasks GROUP BY status")
            counts = dict(c.fetchall())
            conn.close()
            stats = {
                "total": sum(counts.values()),
                "todo": counts.get("todo", 0),
                "in_progress": counts.get("in_progress", 0),
                "completed": counts.get("completed", 0)
            }
            self._send_json(stats)
            return

        # Serve Frontend SPA
        file_to_serve = STATIC_DIR / "index.html"
        if path != "/" and (STATIC_DIR / path.lstrip("/")).exists():
            file_to_serve = STATIC_DIR / path.lstrip("/")

        if file_to_serve.exists():
            content = file_to_serve.read_bytes()
            mime = "text/html" if file_to_serve.suffix == ".html" else "application/octet-stream"
            self.send_response(200)
            self.send_header("Content-Type", mime)
            self.send_header("Content-Length", str(len(content)))
            self.end_headers()
            self.wfile.write(content)
        else:
            self.send_error(404, "File Not Found")

    def do_POST(self):
        if self.path == "/api/tasks":
            length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(length)
            try:
                data = json.loads(body.decode("utf-8"))
            except Exception:
                self._send_json({"error": "Invalid JSON"}, 400)
                return

            title = data.get("title", "").strip()
            if not title:
                self._send_json({"error": "Title is required"}, 400)
                return

            desc = data.get("description", "")
            status = data.get("status", "todo")
            priority = data.get("priority", "medium")

            conn = sqlite3.connect(DB_FILE)
            c = conn.cursor()
            c.execute("INSERT INTO tasks (title, description, status, priority) VALUES (?, ?, ?, ?)", (title, desc, status, priority))
            new_id = c.lastrowid
            conn.commit()
            conn.close()

            self._send_json({"id": new_id, "title": title, "status": status, "priority": priority}, 201)
            return

        self.send_error(404)

    def do_PUT(self):
        if self.path.startswith("/api/tasks/"):
            task_id = self.path.split("/")[-1]
            length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(length)
            data = json.loads(body.decode("utf-8"))

            conn = sqlite3.connect(DB_FILE)
            c = conn.cursor()
            if "status" in data:
                c.execute("UPDATE tasks SET status = ? WHERE id = ?", (data["status"], task_id))
            if "title" in data:
                c.execute("UPDATE tasks SET title = ? WHERE id = ?", (data["title"], task_id))
            conn.commit()
            conn.close()

            self._send_json({"status": "UPDATED", "id": task_id})
            return

        self.send_error(404)


def run(port=8080):
    init_db()
    server_address = ("", port)
    httpd = HTTPServer(server_address, TaskPulseHandler)
    print(f"TaskPulse Pro API & SPA serving on http://localhost:{port}")
    httpd.serve_forever()


if __name__ == "__main__":
    p = int(sys.argv[1]) if len(sys.argv) > 1 else 8080
    run(p)
