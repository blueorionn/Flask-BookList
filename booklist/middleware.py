import os
import datetime
import mysql.connector
from flask import request, redirect


def authentication_middleware():
    """
    Middleware to run before every request.
    """

    # Allow css files even for non logged in user
    if request.path in ["/static/styles/style.css", "/static/styles/base.css"]:
        return

    if request.path == "/auth/login":
        sessionId = str(request.cookies.get("session"))
        if not is_session_id_valid(sessionId):
            return
        else:
            return redirect("/")  # Redirect to home if user logged in.

    if "session" in request.cookies:
        sessionId = str(request.cookies.get("session"))
        if not is_session_id_valid(sessionId):
            return redirect("/auth/login")
        return
    else:
        return redirect("/auth/login")


def is_session_id_valid(sessionId: str):

    # creating database connection
    conn = mysql.connector.connect(
        host=os.environ.get("DB_HOST"),
        database=os.environ.get("DB_NAME"),
        user=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PASSWORD"),
        port=os.environ.get("DB_PORT"),
    )

    # Get a cursor
    cursor = conn.cursor()

    # get session
    cursor.execute(
        "SELECT username, expiry_date FROM sessions WHERE session_id = %s",
        (sessionId,),
    )
    session_data = cursor.fetchone()

    # Closing connection
    cursor.close()
    conn.close()

    if session_data is not None:
        now = datetime.datetime.now()

        if now > list(session_data)[1]:
            return False
        else:
            return True
    else:
        return False
