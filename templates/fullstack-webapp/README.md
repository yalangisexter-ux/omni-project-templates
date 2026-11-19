# Production Full-Stack Web Application Template
### High-Performance Python REST Backend + Reactive SPA + SQLite/PostgreSQL

A modern, production-grade full-stack template with zero external dependency bloat. Ready for Docker, Linux, macOS, and Windows.

---

## Features
- **Backend**: Pure Python Standard Library asynchronous HTTP REST server (`server.py`) or drop-in FastAPI.
- **Database**: SQLite3 with auto-schema creation, table migrations, and sample seed data.
- **Frontend**: Single-Page App (SPA) featuring real-time Kanban workflow, dynamic metric cards, priority filtering, and modal forms.
- **REST APIs**:
  - `GET /health`: Uptime and microservice status.
  - `GET /api/tasks`: Filter tasks by status and priority.
  - `POST /api/tasks`: Create tasks with validation.
  - `PUT /api/tasks/{id}`: Update task properties and status.
  - `GET /api/stats`: Real-time workflow analytics.
- **Containerization**: Includes production `Dockerfile` and `docker-compose.yml`.

---

## Quick Launch
- **Windows**: Double-click `start.bat` or run:
  ```powershell
  python backend\server.py 8080
  ```
- **macOS / Linux**:
  ```bash
  bash start.sh
  ```
- **Docker**:
  ```bash
  docker compose up -d
  ```
Then open `http://localhost:8080` in any web browser!
