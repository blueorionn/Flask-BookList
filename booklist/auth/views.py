"""Auth views."""

from flask import Blueprint, request, render_template, make_response, redirect
from flask.views import MethodView
from .func import authenticate_user, get_userid, create_session

blueprint = Blueprint("auth", __name__, url_prefix="/auth")


class LoginView(MethodView):
    def get(self):
        return render_template("login.html")

    def post(self):
        username = request.form.get("username")
        password = request.form.get("password")

        if authenticate_user(username, password):
            res = make_response(redirect("/"))
            userId = get_userid(username)
            sessionId = create_session(userId, username)
            res.set_cookie("session", sessionId, max_age=3600, httponly=True)
            return res
        else:
            message = {"message": "Username or password is invalid. "}
            return render_template("login.html", **message)


index_view = LoginView.as_view("login")
blueprint.add_url_rule("/login", view_func=index_view)
