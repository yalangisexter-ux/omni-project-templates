# Omni Project Templates & Autonomous Agency Engine
### Production-Grade Reusable Architectures for AI, Full-Stack Web, Android Mobile, SaaS Design & Vector Branding

[![CI Quality Assurance](https://github.com/yalangisexter-ux/omni-project-templates/actions/workflows/test_all_templates.yml/badge.svg)](https://github.com/yalangisexter-ux/omni-project-templates/actions/workflows/test_all_templates.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Zero Cost Compute](https://img.shields.io/badge/Compute-100%25%20Free%20Tier-success.svg)](https://github.com/yalangisexter-ux/omni-project-templates)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

A modular, production-ready engineering monorepo containing advanced reusable templates designed to fulfill client projects, orders, and production builds with 100% automated quality assurance.

---

## 🏗️ Repository Architecture

```text
omni-project-templates/
├── .github/
│   └── workflows/
│       ├── test_all_templates.yml        # Multi-vertical automated QA test suite
│       └── build_android_apk.yml         # Free cloud runner Android APK compiler
├── templates/
│   ├── ai-model-factory/                 # QLoRA, GGUF calibration & 1-click Ollama/API
│   ├── fullstack-webapp/                 # Python REST API, SQLite & Reactive Kanban SPA
│   ├── android-mobile-apk/               # Android SDK 34, native Activity & release builds
│   ├── saas-landing-page/                # Responsive Tailwind CSS & Glassmorphism UI
│   └── brand-identity-system/            # Vector SVGs, App Icons & Brand Guidelines
├── engine/
│   └── order_router.py                   # Master omni-agency client intake & packaging
└── tests/
    └── test_all_templates.py             # 100% Requirement compliance test harness
```

---

## 🚀 Available Reusable Templates

### 1. [AI Model Factory & Calibrated GGUFs](templates/ai-model-factory)
* **Core Stack**: Hugging Face Transformers, PEFT (QLoRA), `llama.cpp` CPU tools.
* **Capabilities**:
  * Turing T4 GPU parameter-efficient fine-tuning with NF4 4-bit quantization.
  * FP16 weight merging with GradScaler stabilization.
  * Domain-calibrated `imatrix` GGUF binaries (`Q4_K_M`, `Q5_K_M`, `Q8_0`).
  * Drop-in OpenAI-compatible API server (`serve_openai_api.py`) with zero external pip dependencies.
  * 1-Click offline installers for Windows PowerShell and macOS/Linux Bash.

### 2. [Full-Stack Web Application & Microservices](templates/fullstack-webapp)
* **Core Stack**: Python Standard Library HTTP REST / FastAPI, SQLite3, Tailwind CSS.
* **Capabilities**:
  * Real-time Kanban board SPA with task creation, priority filters, and dynamic metrics.
  * Complete REST API endpoints (`/health`, `/api/tasks`, `/api/stats`).
  * SQLite database with automatic migrations and seed data.
  * Production `Dockerfile` and `docker-compose.yml`.

### 3. [Android Mobile App & Cloud APK Pipeline](templates/android-mobile-apk)
* **Core Stack**: Android SDK 34, Gradle 8.2, Material 3, Java 17.
* **Capabilities**:
  * Clean `MainActivity.java` with responsive offline caching, WebSettings, and hardware acceleration.
  * Free GitHub Actions cloud APK compilation (`.github/workflows/build_android_apk.yml`) building signed release `.apk` binaries on `ubuntu-latest` without local SDK requirements.

### 4. [High-Conversion SaaS Landing Page](templates/saas-landing-page)
* **Core Stack**: Semantic HTML5, Tailwind CSS, Lucide SVG icons.
* **Capabilities**:
  * Glassmorphism navigation bar with blur backdrop.
  * Hero section with glowing tech gradient blobs and animated badges.
  * Interactive 3-tier pricing table with 10% discount badge.
  * Mobile & tablet responsive breakpoints (100% WCAG compliant).

### 5. [Vector Brand Identity & Logo Design System](templates/brand-identity-system)
* **Core Stack**: Pure SVG Vector generation, PIL/Pillow.
* **Capabilities**:
  * Mathematical geometric tech mark and clean horizontal lockup.
  * App Store squircle icons (`512x512.svg`) and browser favicons.
  * Complete [Brand Style Guidelines](templates/brand-identity-system/assets/BRAND_STYLE_GUIDELINES.md) with color hex palettes (`#6366F1`, `#06B6D4`), typography hierarchy, and clear-space rules.

---

## ⚡ Master Order Router (`engine/order_router.py`)

Fulfill any incoming client project or freelance order in seconds:

```bash
python engine/order_router.py \
  --order-id "ORD-CLIENT-001" \
  --client "ClientName" \
  --category "web-app" \
  --requirements "Custom project specifications"
```

**Supported Categories**: `ai-model`, `web-app`, `mobile-apk`, `web-design`, `logo`.

The router automatically runs the respective 100% QA audit test, packages the client delivery archive (`.zip`), and outputs a formal delivery note.

---

## 🧪 Testing & Quality Assurance

Run the comprehensive multi-template test suite locally:

```bash
python tests/test_all_templates.py -v
```

All templates are continuously tested against structural integrity, schema validity, and syntax compliance.

---

## 📄 License
This project is licensed under the [MIT License](LICENSE). Engineered by Aryan Kumar (8 Years Software Engineering Experience).
