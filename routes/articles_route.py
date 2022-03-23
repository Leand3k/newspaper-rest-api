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
    return '', 204