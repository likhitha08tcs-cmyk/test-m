import os

SECRET_KEY = os.environ["SECRET_KEY"]
DB_URL = os.environ["DB_URL"]
DEBUG = os.environ.get("DEBUG", "false")
