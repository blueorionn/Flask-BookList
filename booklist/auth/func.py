import os
import uuid
import bcrypt
import datetime
from datetime import timedelta
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
    conn.commit()
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


def get_userid(username: str):
    """Get UserId By Username"""
    query = """
        SELECT id FROM users WHERE username = %s
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
    userid = cursor.fetchone()

    # Closing connection
    conn.commit()
    cursor.close()
    conn.close()

    return str(list(userid)[0]) or None


def create_session(userid: str, username: str):
    """Create user session"""

    query = """
        INSERT INTO sessions (
            session_id,
            user_id,
            username,
            creation_date,
            expiry_date
        ) VALUES (
            %s,
            %s,
            %s,
            %s,
            %s
        )
    """

    session_id = str(uuid.uuid4())
    creation_date = datetime.datetime.now()
    # Session id valid till 1 hour.
    expiry_date = creation_date + timedelta(hours=1)

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

    # Create session
    cursor.execute(
        query,
        (session_id, userid, username, creation_date, expiry_date),
    )

    # Closing connection
    conn.commit()
    cursor.close()
    conn.close()

    return session_id
