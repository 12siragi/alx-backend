#!/usr/bin/env python3
"""
    Basic Flask app with Babel setup.
"""

from flask import Flask, render_template
from flask_babel import Babel

class Config:
    """
    Config class to configure Babel and the app.
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app = Flask(__name__, static_url_path='')
app.config.from_object(Config)

# Instantiate the Babel object
babel = Babel(app)

@app.route('/', strict_slashes=False)
def index() -> str:
    """This route renders the index page with Babel support."""
    return render_template('1-index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

