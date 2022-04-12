from flask import request, Blueprint, Response
from werkzeug.utils import secure_filename

from models import article
from app import db
from models.article import Article, article_schema, articles_schema
import codecs

articleRoute = Blueprint("articleRoute", __name__)


@articleRoute.route("/article/create", methods=["POST"])
def add_article():
    article.Article.title = request.form["title"]
    article.Article.body = request.form["body"]
    article.Article.author = request.form["author"]
    article.Article.categoria = request.form["categoria"]
    multimedia = request.files["multimedia"]
    if not multimedia:
        return "No picture uploaded", 400

    filename = secure_filename(multimedia.filename)
    article.Article.filename = filename
    mimetype = multimedia.mimetype
    article.Article.mimetype = mimetype
    article.Article.data = multimedia
    if not filename:
        return "Bad Upload!!", 400

    # data = article.Article(article.Article.filename, article.Article.data.read(), article.Article.mimetype)

    new_article = article.Article(
        article.Article.title,
        article.Article.body,
        article.Article.author,
        article.Article.categoria,
        article.Article.filename,
        article.Article.data.read(),
        article.Article.mimetype

    )
    db.session.add(new_article)
    db.session.commit()
    return article.article_schema.jsonify(new_article)


@articleRoute.route("/article/<int:idArticle>")
def get_article(idArticle):
    returnable = db.session.query(Article).get(idArticle)
    returnable.data = codecs.encode(returnable.data, 'base64').decode('utf-8')
    base64 = f"data:{returnable.mimetype};base64,{returnable.data}"
    returnable.data = base64
    return article_schema.dump(returnable)


@articleRoute.route("/article/all")
def get_all_article():
    returnable = Article.query.all()
    for article in returnable:
        article.data = codecs.encode(article.data, 'base64').decode('utf-8')
        base64 = f"data:{article.mimetype};base64,{article.data}"
        article.data = base64
    return articles_schema.jsonify(returnable)


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
    return article_schema.dump(returnable), 200
