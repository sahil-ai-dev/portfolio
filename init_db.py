"""
Database initialization and seeding script for Sahil Razza's Portfolio.
Run this script once to create tables and populate initial verified data.
Usage:
    python init_db.py
"""

import os
import sys
import getpass
from app import create_app
from app.extensions import db
from app.models.user import User
from app.models.project import Project
from app.models.skill import Skill
from app.models.education import Education
from app.models.site_setting import SiteSetting


def init_database():
    app = create_app('development')
    with app.app_context():
        print("🔧 Creating database tables...")
        db.create_all()
        print("✅ Tables created.")

        # 1. Seed Site Settings
        print("🌱 Seeding portfolio settings...")
        settings_defaults = {
            'owner_name': 'Sahil Razza',
            'hero_heading': "Hey, I'm Sahil",
            'professional_title': 'AI/ML Student | Aspiring AI Engineer',
            'short_intro': "I'm an AI/ML student exploring programming, software development, and intelligent systems. I'm building projects, learning new technologies, and working toward becoming an AI engineer.",
            'about_text': "I am currently a second-year engineering student pursuing a B.Tech in Artificial Intelligence and Machine Learning. My passion lies in understanding how intelligent systems work from first principles. From foundational C programming to Python software and machine learning models, I am dedicated to continuous learning and building high-impact software solutions.",
            'github_url': 'https://github.com/sahilrazza',
            'linkedin_url': 'https://linkedin.com/in/sahilrazza',
            'instagram_url': 'https://instagram.com',
            'contact_email': 'sahil@example.com',
            'profile_image': 'images/profile_placeholder.svg',
            'resume_file': 'files/resume.pdf'
        }
        for key, val in settings_defaults.items():
            if not SiteSetting.query.filter_by(key=key).first():
                db.session.add(SiteSetting(key=key, value=val))

        # 2. Seed Skills (Honest developing skills)
        if Skill.query.count() == 0:
            print("🌱 Seeding verified skill cards...")
            verified_skills = [
                # Programming Languages
                Skill(name="Python", category="Programming Languages", proficiency_level="Developing", icon="terminal", display_order=1),
                Skill(name="C", category="Programming Languages", proficiency_level="Foundational", icon="cpu", display_order=2),
                Skill(name="JavaScript", category="Programming Languages", proficiency_level="Foundational", icon="code", display_order=3),
                
                # Frontend Development
                Skill(name="HTML5 & Semantic Markup", category="Frontend Development", proficiency_level="Developing", icon="layout", display_order=1),
                Skill(name="CSS3 & Futuristic UI", category="Frontend Development", proficiency_level="Developing", icon="palette", display_order=2),
                Skill(name="Responsive Web Design", category="Frontend Development", proficiency_level="Foundational", icon="smartphone", display_order=3),

                # Backend Development
                Skill(name="Flask Web Framework", category="Backend Development", proficiency_level="Developing", icon="server", display_order=1),
                Skill(name="RESTful API Design", category="Backend Development", proficiency_level="Foundational", icon="network", display_order=2),

                # Databases
                Skill(name="SQLite", category="Databases", proficiency_level="Developing", icon="database", display_order=1),
                Skill(name="SQL Queries & Modeling", category="Databases", proficiency_level="Foundational", icon="hard-drive", display_order=2),

                # AI/ML Learning
                Skill(name="AI/ML Fundamentals", category="AI/ML Learning", proficiency_level="Learning & Exploring", icon="brain", display_order=1),
                Skill(name="Neural Network Concepts", category="AI/ML Learning", proficiency_level="Learning & Exploring", icon="share-2", display_order=2),
                Skill(name="Python Math & Data Tools", category="AI/ML Learning", proficiency_level="Foundational", icon="bar-chart-2", display_order=3),

                # Developer Tools
                Skill(name="VS Code IDE", category="Developer Tools", proficiency_level="Developing", icon="code", display_order=1),
                Skill(name="Git & Version Control", category="Developer Tools", proficiency_level="Learning & Exploring", icon="git-branch", display_order=2),
                Skill(name="Command Line & PowerShell", category="Developer Tools", proficiency_level="Developing", icon="terminal", display_order=3)
            ]
            db.session.add_all(verified_skills)

        # 3. Seed Education (Verified: 2nd year B.Tech in AI & ML)
        if Education.query.count() == 0:
            print("🌱 Seeding education timeline...")
            edu = Education(
                institution="Engineering College / University",
                degree="B.Tech in Artificial Intelligence & Machine Learning",
                field_of_study="Artificial Intelligence & Machine Learning",
                start_year="2024",
                end_year="2028 (Expected)",
                is_current=True,
                description="Currently in 2nd year. Core coursework includes Data Structures & Algorithms, Object Oriented Programming, Discrete Mathematics, Operating Systems, and Machine Learning Principles.",
                display_order=1
            )
            db.session.add(edu)

        # 4. Seed Projects (Honest initial educational projects)
        if Project.query.count() == 0:
            print("🌱 Seeding starter projects...")
            starter_projects = [
                Project(
                    title="Futuristic AI/ML Developer Portfolio",
                    category="Web",
                    description="A high-performance, responsive full-stack developer portfolio built with Python Flask, SQLite, and Three.js 3D visuals. Features an authenticated admin CMS, CSRF protection, and a verified portfolio FAQ chatbot.",
                    tech_stack="Python, Flask, SQLite, Three.js, CSS3, Jinja2",
                    github_url="https://github.com",
                    demo_url="#",
                    is_featured=True,
                    display_order=1
                ),
                Project(
                    title="Machine Learning Foundations & Algorithms",
                    category="AI/ML",
                    description="Exploratory implementations of core machine learning concepts from scratch, including linear regression, gradient descent optimization, and evaluation metrics.",
                    tech_stack="Python, NumPy, Matplotlib, Jupyter",
                    github_url="https://github.com",
                    demo_url="",
                    is_featured=True,
                    display_order=2
                ),
                Project(
                    title="C Algorithms & Memory Management Lab",
                    category="Systems",
                    description="A structured collection of low-level algorithms, dynamic memory allocation practices, and data structures (linked lists, stacks, trees) implemented in standard C.",
                    tech_stack="C, GCC, Data Structures",
                    github_url="https://github.com",
                    demo_url="",
                    is_featured=False,
                    display_order=3
                )
            ]
            db.session.add_all(starter_projects)

        # 5. Admin User Setup
        admin_user = User.query.filter_by(is_admin=True).first()
        if not admin_user:
            env_user = os.getenv('ADMIN_USERNAME')
            env_pass = os.getenv('ADMIN_PASSWORD')
            env_email = os.getenv('ADMIN_EMAIL')

            if env_user and env_pass:
                print(f"👤 Creating admin from environment variables ({env_user})...")
                u = User(username=env_user, email=env_email or f"{env_user}@portfolio.local")
                u.set_password(env_pass)
                db.session.add(u)
            elif sys.stdin.isatty():
                print("\n🔐 Initial Admin User Setup")
                print("No admin account exists yet. Let's create one now.")
                username = input("Enter admin username [default: sahil]: ").strip() or "sahil"
                email = input("Enter admin email [default: sahil@portfolio.local]: ").strip() or "sahil@portfolio.local"
                password = getpass.getpass("Enter strong admin password: ").strip()
                while not password or len(password) < 6:
                    print("Password must be at least 6 characters.")
                    password = getpass.getpass("Enter strong admin password: ").strip()
                u = User(username=username, email=email)
                u.set_password(password)
                db.session.add(u)
            else:
                import secrets
                random_pass = secrets.token_urlsafe(16)
                auto_user = "admin"
                print(f"⚠️  Non-interactive mode: Generating secure one-time admin credentials.")
                print(f"👉 Username: {auto_user}")
                print(f"👉 Generated Password: {random_pass}")
                print("💡 Tip: Set ADMIN_USERNAME and ADMIN_PASSWORD in your .env file or change this password upon login.")
                u = User(username=auto_user, email="admin@portfolio.local")
                u.set_password(random_pass)
                db.session.add(u)

        db.session.commit()
        print("✨ Database setup complete!")


if __name__ == '__main__':
    init_database()

