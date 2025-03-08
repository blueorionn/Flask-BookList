"""Auth views."""

from flask import Blueprint, render_template
from flask.views import MethodView


blueprint = Blueprint("auth", __name__, url_prefix="/auth")


class IndexView(MethodView):
    def get(self):
        return render_template("login.html")


index_view = IndexView.as_view("home")
blueprint.add_url_rule("/login", view_func=index_view)
