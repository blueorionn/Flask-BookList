"""Core views."""

import os
from flask import current_app, Blueprint, render_template, send_file
from flask.views import MethodView
from .func import list_books
from booklist.utils import hyphenate_text

blueprint = Blueprint("core", __name__)


class IndexView(MethodView):
    def get(self):
        context = {"message": "Fetched All books"}
        book_list = list_books()

        # additional computation
        books = []
        for book in book_list:
            b = {}
            b["id"] = list(book)[0]
            b["title"] = list(book)[1]
            b["summary"] = list(book)[2]
            b["ISBN"] = list(book)[3]
            b["genre"] = list(book)[4]
            b["publication_year"] = list(book)[5]
            b["author"] = list(book)[6]
            b["publisher"] = list(book)[7]
            b["rating"] = list(book)[8]
            b["thumbnail"] = f"/book/thumbnail/{hyphenate_text(list(book)[1])}.jpg"

            books.append(b)

        context["books"] = books
        return render_template("index.html", **context)


@blueprint.route("/book/thumbnail/<filename>")
def serve_thumbnail(filename):
    path = os.path.join(current_app.config["APP_DIR"], f"assets/{filename}")

    return send_file(path, mimetype="image/jpg")


index_view = IndexView.as_view("home")
blueprint.add_url_rule("/", view_func=index_view)
