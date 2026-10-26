# Sahil Razza — Futuristic AI/ML Developer Portfolio

A complete, production-minded full-stack developer portfolio and content management system built from scratch with **Python Flask**, **SQLite**, and lightweight **Three.js** 3D visuals.

---

## 🌟 Features Overview

- **Futuristic & Responsive Design System**:
  - Deep space navy background (`#070b14`), electric blue accents (`#0066ff`), and cyan highlights (`#00f0ff`).
  - Subtle glassmorphism, glowing borders, and crisp typography.
  - Interactive neural constellation particle visual powered by Three.js with WebGL capability detection.
  - Reduced-motion accessibility mode (`prefers-reduced-motion`) and functional Dark/Light theme toggle.
  - Responsive layouts optimized for desktop, tablet, and mobile screens.
- **Dynamic Content Sections**:
  - **Hero Section**: Live typing animation, honest credentials, social profile badges, and call-to-action buttons.
  - **About Section**: Educational overview, AI/ML focus areas, and honest learning trajectory.
  - **Skills Section**: Categorized competencies (Programming Languages, Frontend, Backend, Databases, AI/ML Learning, Tools) with honest proficiency indicators.
  - **Education Timeline**: Verified degree progression in B.Tech Artificial Intelligence & Machine Learning.
  - **Projects Showcase**: Interactive project cards with live category filters (AI/ML, Web, Systems), technology tags, GitHub code links, and demo buttons.
  - **Resume Section**: Dedicated resume preview modal in the browser and one-click PDF download handler.
  - **Contact Section**: Secure, CSRF-protected contact form with real-time AJAX feedback and client/server validation.
- **Protected Admin CMS Dashboard**:
  - Authenticated admin login and session management via `Flask-Login` and `Werkzeug` secure password hashing.
  - Complete project management (Create, Read, Update, Delete).
  - Skill and education timeline managers.
  - Inbound messages inbox: view submissions, toggle read/unread status, and delete inquiries.
  - Site settings manager: update headline copy, bio, contact email, social profile URLs, and upload new resume PDFs or profile photos without editing code.
- **Portfolio AI Chatbot**:
  - Lightweight, deterministic FAQ knowledge engine that answers verified questions about Sahil's studies, skills, projects, and contact channels.
  - Zero external costs and zero hallucination risk.
  - Future-ready adapter interface for external LLM APIs (Google Gemini, OpenAI, etc.).
- **Optional GitHub Integration**:
  - Service client that queries public repositories via the GitHub REST API with in-memory caching and graceful fallback.

---

## 🛠️ Technology Stack

| Layer | Technologies |
| :--- | :--- |
| **Backend Framework** | Python 3 (Flask WSGI) |
| **Database & ORM** | SQLite & Flask-SQLAlchemy |
| **Authentication & Security** | Flask-Login, Werkzeug Security, Flask-WTF (CSRF Protection) |
| **Frontend Templates & UI** | Jinja2, HTML5 Semantic Elements, Modern CSS3 Variables |
| **Interactive 3D Visuals** | Three.js (r128) Particle Constellation |
| **Form Validation** | WTForms & email-validator |
| **Automated Testing** | pytest (17 automated route, auth, CRUD, and CSRF tests) |

---

## 📁 Project Directory Structure

```
sahil.portfolio/
├── app/
│   ├── __init__.py               # Flask application factory (create_app)
│   ├── config.py                 # Development, Testing, Production configurations
│   ├── extensions.py             # SQLAlchemy, LoginManager, CSRFProtect singletons
│   ├── forms.py                  # WTForms form classes with validators
│   │
│   ├── models/                   # SQLAlchemy database schemas
│   │   ├── user.py               # Admin user model (password hashing)
│   │   ├── project.py            # Project showcase model
│   │   ├── skill.py              # Categorized skills model
│   │   ├── education.py          # Education history model
│   │   ├── contact.py            # Contact message storage
│   │   └── site_setting.py       # Dynamic bio, headlines, and links
│   │
│   ├── routes/                   # Modular Blueprints
│   │   ├── main.py               # Public portfolio pages & contact submissions
│   │   ├── admin.py              # Protected dashboard & CRUD actions
│   │   └── api.py                # Chatbot & GitHub endpoints
│   │
│   ├── services/                 # Reusable business logic
│   │   ├── chatbot.py            # Verified FAQ engine & AI API adapter
│   │   └── github_service.py     # GitHub REST API client with caching
│   │
│   ├── static/                   # Static Frontend Assets
│   │   ├── css/
│   │   │   ├── style.css         # Public futuristic design system
│   │   │   └── admin.css         # Admin dashboard layout
│   │   ├── js/
│   │   │   ├── main.js           # Theme toggle, typing effect, AJAX, modal
│   │   │   ├── chatbot.js        # Chatbot widget client
│   │   │   └── three-scene.js    # 3D neural constellation with WebGL fallback
│   │   ├── images/
│   │   │   ├── profile.png       # User photo (or placeholder)
│   │   │   └── profile_placeholder.svg # High-tech cyber avatar fallback
│   │   └── files/
│   │       └── resume.pdf        # User resume PDF
│   │
│   └── templates/                # Jinja2 Templates
│       ├── base.html             # Master skeleton with navbar & footer
│       ├── index.html            # Main portfolio one-page landing
│       ├── chatbot_widget.html   # Embeddable assistant widget
│       ├── errors/               # Custom 404 and 500 error pages
│       └── admin/                # Admin templates (login, dashboard, projects, etc.)
│
├── instance/                     # Local SQLite database & uploads (git-ignored)
│   ├── portfolio.db
│   └── uploads/
│
├── tests/                        # Automated Pytest suite
│   ├── conftest.py
│   ├── test_routes.py
│   ├── test_auth.py
│   ├── test_projects.py
│   └── test_contact.py
│
├── .env.example                  # Environment configuration template
├── .env                          # Local environment secrets (git-ignored)
├── .gitignore                    # Git ignore file
├── requirements.txt              # Pinned Python package dependencies
├── run.py                        # Local development runner
└── init_db.py                    # Database creation & initial admin setup script
```

---

## 🚀 Local Setup & Installation

### Step 1: Open Terminal in Workspace
Make sure your terminal is opened in the project root:
```powershell
cd c:\Users\sahil\sahil.portfolio
```

### Step 2: Virtual Environment Activation
A virtual environment has already been created for you in `.venv/`. To activate it:

**In PowerShell:**
```powershell
.\.venv\Scripts\Activate.ps1
```

*(If PowerShell displays an execution policy restriction, run: `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`)*

**In Command Prompt (cmd):**
```cmd
.\.venv\Scripts\activate.bat
```

### Step 3: Install Dependencies (If setting up fresh)
```powershell
python -m pip install -r requirements.txt
```

### Step 4: Environment Configuration & Database Initialization

1. Create your local environment configuration file from the template:
   ```powershell
   Copy-Item .env.example .env
   ```

2. Open `.env` and configure your secret key and preferred admin credentials:
   ```ini
   SECRET_KEY=your-secure-random-secret-key
   ADMIN_USERNAME=your_admin_username
   ADMIN_PASSWORD=your_strong_admin_password
   ADMIN_EMAIL=your_email@example.com
   ```

3. Initialize the database and create your administrative account:
   ```powershell
   python init_db.py
   ```
   *(If `ADMIN_USERNAME` and `ADMIN_PASSWORD` are not defined in `.env`, the script will interactively and securely prompt you for your username and password in the terminal).*

---

## 💻 Running the Application

Start the development server with:
```powershell
python run.py
```

Output:
```
============================================================
🚀  SAHIL RAZZA — FUTURISTIC AI/ML PORTFOLIO
============================================================
📡 Local server running at: http://127.0.0.1:5000
🔐 Admin dashboard at:      http://127.0.0.1:5000/admin
⚙️  Environment:             development
🛑 Press Ctrl+C in terminal to stop the server.
============================================================
```

- Open **http://127.0.0.1:5000** in your browser to view the portfolio.
- Open **http://127.0.0.1:5000/admin** to access the Admin Control Console using the credentials you configured.

To **stop the server**, simply press `Ctrl + C` in the terminal.

---

## 🧪 Running Automated Tests

Run the full automated test suite (20 comprehensive tests):
```powershell
python -m pytest -v
```

All 20 tests verify:
- Public routes availability and response rendering.
- Custom 404 error page.
- Admin authentication & unauthorized route redirection.
- Project CRUD operations.
- Contact form server-side validation & AJAX handling.
- Chatbot knowledge response accuracy.
- Profile photo and resume PDF serving endpoints.
- Contact form server-side validation & AJAX handling.
- Chatbot knowledge response accuracy.

---

## 📸 Managing Your Personal Assets

### 1. Adding Your Real Profile Photo
You have two easy options:
- **Option A (Via Admin Dashboard)**: Go to **http://127.0.0.1:5000/admin/settings**, choose your photo under **Upload Profile Photograph**, and click **Save**.
- **Option B (Direct File Copy)**: Copy your photo file to `app/static/images/profile.png`. The app will automatically display your real photograph with the cyber frame glow.

### 2. Adding Your Resume PDF
- **Option A (Via Admin Dashboard)**: Go to **http://127.0.0.1:5000/admin/settings**, choose your PDF under **Upload Resume PDF Document**, and click **Save**.
- **Option B (Direct File Copy)**: Copy your PDF to `app/static/files/resume.pdf`. The website's **Download Resume** button and browser **Preview** modal will activate immediately.

### 3. Configuring Social Profiles
In **http://127.0.0.1:5000/admin/settings**, you can edit your GitHub, LinkedIn, and Instagram profile URLs.

---

## 🔒 Security Best Practices

1. **No Plaintext Passwords**: All user passwords are encrypted using `scrypt` hashing via `werkzeug.security`.
2. **CSRF Protection**: All mutating forms require valid CSRF tokens via `Flask-WTF`.
3. **Session Cookies**: Session cookies are configured with `HttpOnly` and `SameSite=Lax`.
4. **Parameterized Queries**: All database queries use SQLAlchemy to prevent SQL injection.
5. **File Upload Restrictions**: File uploads enforce strict extension checks (`.png`, `.jpg`, `.pdf`) and a 5MB size limit.
6. **Git Safety**: `.gitignore` ensures your `.env` secrets, virtual environment, and local `.db` files are never committed to public repositories.

---

## 🌐 Future Deployment Guide (Production)

When you are ready to deploy your portfolio publicly (e.g., on Render, Railway, or VPS):

1. **Production WSGI Server**:
   - Use `gunicorn` on Linux: `gunicorn "app:create_app('production')"`
   - For servers expecting an application object, set `FLASK_ENV=production` and use `gunicorn run:app` (or `gunicorn app:app`).
2. **Environment Variables**:
   - Set `FLASK_ENV=production`
   - Set a strong, randomly generated `SECRET_KEY` (e.g. generated via `python -c "import secrets; print(secrets.token_hex(32))"`).
   - Set `SESSION_COOKIE_SECURE=True` to enforce HTTPS cookies.
3. **Persistent Storage for SQLite & Uploads**:
   - Cloud platforms often have ephemeral filesystems. If using SQLite, attach a **Persistent Disk/Volume** to the `/instance` directory so that contact messages and uploaded files persist across server restarts.
   - Alternatively, configure PostgreSQL by providing a `DATABASE_URL=postgresql://...` connection string.
4. **HTTPS / SSL**:
   - Ensure the hosting provider (e.g. Render, Cloudflare) provides automatic SSL certificates for secure HTTPS traffic.

---

## 🐙 Publishing to GitHub (Pre-flight Checklist)

Before pushing this repository to GitHub:

1. **Verify Ignored Files**:
   Ensure `.env`, `.venv/`, and `instance/` (containing `portfolio.db`) are NOT tracked by Git:
   ```powershell
   git status
   ```
   *Only clean project source files, `static/` assets (including `profile.jpeg` and `resume.pdf`), templates, and `.env.example` should be listed.*

2. **Initialize Git (if not already done)**:
   ```powershell
   git init
   git add .
   git commit -m "Initial commit: Futuristic AI/ML developer portfolio"
   ```

3. **Link to GitHub & Push**:
   ```powershell
   git branch -M main
   git remote add origin https://github.com/<your-username>/<your-repo-name>.git
   git push -u origin main
   ```

