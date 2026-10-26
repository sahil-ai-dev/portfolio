import os
from app import app


def _coerce_int(value, default):
    """Return an integer from an environment value, falling back on a default."""
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


# Load appropriate configuration (development, production, testing)
env = os.getenv('FLASK_ENV', 'development').strip().lower() or 'development'

if __name__ == '__main__':
    port = _coerce_int(os.getenv('PORT', 5000), 5000)
    host = os.getenv('HOST', '127.0.0.1')
    default_debug = '1' if app.config.get('DEBUG', False) else '0'
    debug = str(os.getenv('FLASK_DEBUG', default_debug)).lower() in {'1', 'true', 'yes', 'on'}

    print("\n" + "="*60)
    print("🚀  SAHIL RAZZA — FUTURISTIC AI/ML PORTFOLIO")
    print("="*60)
    print(f"📡 Local server running at: http://{host}:{port}")
    print(f"🔐 Admin dashboard at:      http://{host}:{port}/admin")
    print(f"⚙️  Environment:             {env}")
    print("🛑 Press Ctrl+C in terminal to stop the server.")
    print("="*60 + "\n")

    app.run(host=host, port=port, debug=debug)
