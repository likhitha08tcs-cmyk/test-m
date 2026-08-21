import os

SECRET_KEY = os.environ.get("SECRET_KEY", "safe_default")
DB_URL = os.environ.get("DB_URL", "safe_default")
DEBUG = os.environ.get("DEBUG", "false")
