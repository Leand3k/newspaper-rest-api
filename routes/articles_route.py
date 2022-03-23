import json

from flask import request, Response, jsonify, Blueprint
from models import article
from app import db
from models.article import Article, article_schema

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


@articleRoute.route("/article/<int:idArticle>")
def get_article(idArticle):
    returnable = Article.query.get_or_404(idArticle)
    return article_schema.dump(returnable)


@articleRoute.route("/article/delete/<int:idArticle>", methods=["DELETE"])
def delete_article(idArticle):
    returnable = Article.query.get_or_404(idArticle)
    db.session.delete(returnable)
    db.session.commit()
    return "", 204


@articleRoute.route("/article/edit/<int:idArticle>", methods=["POST"])
def edit_article(idArticle):
    returnable = Article.query.get_or_404(idArticle)

    if "title" in request.form:
        returnable.title = request.form["title"]
    if "body" in request.form:
        returnable.body = request.form["body"]
    if "author" in request.form:
        returnable.author = request.form["author"]

    db.session.commit()
    return article_schema.dump(returnable)
