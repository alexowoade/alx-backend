#!/usr/bin/env python3
"""Basic Babel Setup"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Config class for flask app
    """
    DEBUG = True
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

# use this below instead of @babel.localeselector /
# for modern versions of babel
# babel.init_app(app, locale_selector=get_locale)


@app.route('/')
def index():
    """view function for root route

    Returns:
        html: homepage
    """
    return render_template('4-index.html')


@babel.localeselector
def get_locale():
    """get best language match

    Returns:
        str: best match
    """
    locale = request.args.get("locale")
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run()
