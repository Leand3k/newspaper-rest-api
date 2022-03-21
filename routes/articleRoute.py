from flask import request, jsonify, Blueprint
from models import article
from app import db

articleRoute = Blueprint("articleRoute", __name__)


@articleRoute.route("/article", methods=["POST"])
def add_article():
    article.Article.title = request.form["title"]
    article.Article.body = request.form["body"]
    article.Article.author = request.form["author"]

    new_article = article.Article(
        article.Article.title, article.Article.body, article.Article.author
    )
    db.session.add(new_article)
    db.session.commit()
    return article.article_schema.jsonify(new_article)
