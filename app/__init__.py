from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

db = SQLAlchemy()
migrate = Migrate()
load_dotenv()

def create_app(test_config=None):
    app = Flask(__name__)

    if not test_config:
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
            "SQLALCHEMY_DATABASE_URI")
    else:
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
            "SQLALCHEMY_TEST_DATABASE_URI")

    # Import models here
    from app.models.book import Book
    from app.models.author import Author

    db.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprints here
    # from .book_routes import bp as books_bp
    # app.register_blueprint(books_bp)

    # from .author_routes import bp as authors_bp
    # app.register_blueprint(authors_bp)

    # Register blueprints
    from .routes import book
    from .routes import author
    app.register_blueprint(book.bp)
    app.register_blueprint(author.bp)

    return app