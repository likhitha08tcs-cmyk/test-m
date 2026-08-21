import os
os.environ.setdefault("SECRET_KEY", "test-secret")
os.environ.setdefault("DB_URL", "sqlite:///test.db")

import app.config as config

def test_secret_key_loaded():
    assert config.SECRET_KEY is not None
    assert config.SECRET_KEY != ""

def test_db_url_loaded():
    assert config.DB_URL is not None
    assert config.DB_URL != ""

def test_debug_default():
    assert config.DEBUG in ("true", "false")
