from app import db
from app.models.author import Author
from flask import Blueprint, jsonify, abort, make_response, request

authors_bp = Blueprint("author_bp", __name__, url_prefix="/authors")

@authors_bp.route("", methods=["POST"])
def create_author():
    request_body = request.get_json()
    new_author = Author.from_dict(request_body)

    db.session.add(new_author)
    db.session.commit()

    return make_response(jsonify(f"Author {new_author.name} successfully created"), 201)

@authors_bp.route("", methods=["GET"])
def read_all_authors():
    name_query = request.args.get("name")
    author_query = Author.query

    if name_query:
        author_query = Author.query.filter_by(name=name_query)

    authors = author_query.all()

    authors_response = [author.to_dict() for author in authors]
    return jsonify(authors_response)