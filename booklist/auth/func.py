import os
import bcrypt
import mysql.connector
from booklist.utils import is_valid_uuid_v4


def authenticate_user(username: str, password: str):
    """Check if user exists with valid credentials."""

    query = """
        SELECT id,username,password FROM users WHERE username = %s
    """

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

    # get user
    cursor.execute(
        query,
        (username,),
    )
    user = cursor.fetchone()

    # Closing connection
    cursor.close()
    conn.close()

    # If user exist
    if user is not None:
        # Checking if password is correct
        fetched_user_id, fetched_username, fetched_password = (
            list(user)[0],
            list(user)[1],
            list(user)[2],
        )

        if (
            (bcrypt.checkpw(password.encode("utf-8"), fetched_password.encode("utf-8")))
            and (username == fetched_username)
            and is_valid_uuid_v4(fetched_user_id)
        ):
            return True
        else:
            return False
    else:
        return False
