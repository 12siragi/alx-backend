# Flask i18n Project

## Description

This project demonstrates the use of Flask and Babel to implement internationalization (i18n) in a web application. It covers the basics of setting up a Flask app, configuring Babel for language and timezone localization, and handling user preferences for locale and timezone.

## Features

- Basic Flask application setup.
- Babel integration for i18n support.
- Language selection based on request headers, URL parameters, and user settings.
- Template parameterization for translated content.
- Mock user login system to demonstrate locale and timezone preferences.
- Flask templates with localized messages.

## Project Structure

```bash
.
├── 0-app.py
├── 1-app.py
├── 2-app.py
├── 3-app.py
├── 4-app.py
├── 5-app.py
├── 6-app.py
├── 7-app.py
├── babel.cfg
├── templates/
│   ├── 0-index.html
│   ├── 1-index.html
│   ├── 2-index.html
│   ├── 3-index.html
│   ├── 4-index.html
│   ├── 5-index.html
│   ├── 6-index.html
│   └── 7-index.html
├── translations/
│   ├── en/
│   │   └── LC_MESSAGES/
│   │       ├── messages.po
│   │       └── messages.mo
│   ├── fr/
│   │   └── LC_MESSAGES/
│   │       ├── messages.po
│   │       └── messages.mo
└── README.md

