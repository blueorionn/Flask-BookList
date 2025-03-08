"""User registration script"""

import os
import uuid
import argparse
import bcrypt
import sys
import mysql.connector
import datetime


def create_user_table():
    query = """
        CREATE TABLE IF NOT EXISTS users (
            id VARCHAR(36) PRIMARY KEY,
            first_name VARCHAR(255) UNIQUE,
            last_name VARCHAR(255) NULL,
            username VARCHAR(255) UNIQUE,
            password VARCHAR(60),
            role VARCHAR(255),
            created_at DATETIME
        )
    """
    return query


def get_create_user_query():
    query = """
        INSERT INTO users (
            id,
            first_name,
            last_name,
            username,
            password,
            role,
            created_at
        ) VALUES (
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s
        )
    """

    return query


def main():
    DB_HOST = os.environ.get("DB_HOST")
    DB_NAME = os.environ.get("DB_NAME")
    DB_USER = os.environ.get("DB_USER")
    DB_PASSWORD = os.environ.get("DB_PASSWORD")
    DB_PORT = os.environ.get("DB_PORT")

    if DB_HOST == None or len(DB_HOST) < 1:
        raise ValueError("Invalid or emtpy db host")
    if DB_NAME == None or len(DB_NAME) < 1:
        raise ValueError("Invalid or emtpy db name")
    if DB_USER == None or len(DB_USER) < 1:
        raise ValueError("Invalid or empty db user")
    if DB_PASSWORD == None or len(DB_PASSWORD) < 1:
        raise ValueError("Invalid or emtpy db password")
    if DB_PORT == None or len(DB_PORT) < 1:
        raise ValueError("Invalid or emtpy db port")

    # Add arguments
    parser = argparse.ArgumentParser(
        prog="Register Users",
        description=("Register users by creating data row in users table."),
        epilog="User Created! :)",
    )
    parser.add_argument("-fn", "--first-name", help="Firstname of the user.")
    parser.add_argument("-ln", "--last-name", help="Lastname of the user.")
    parser.add_argument("-u", "--username", help="Username of the user.")
    parser.add_argument(
        "-p", "--password", help="Password of the user. Minimum 8 char long."
    )
    parser.add_argument(
        "-r", "--role", help="Role of the user. Available role admin or user."
    )
    args = parser.parse_args()

    # Get Arguments
    id = str(uuid.uuid4())
    first_name: str = args.first_name
    last_name: str = args.last_name
    user_name: str = args.username
    password: str = args.password
    role: str = args.role
    created_at = datetime.datetime.now()

    # Check argument validity
    if first_name == None or len(first_name) < 1:
        raise ValueError("Invalid or empty Firstname. Arguments -fn or --first-name")
    if user_name == None or len(user_name) < 1:
        raise ValueError("Invalid or empty Username. Arguments -u or --username")
    if last_name == None or len(last_name) < 1:
        # lastname is not required
        last_name = None
    if password == None or len(password) < 8:
        raise ValueError(
            "Invalid or empty Password. Arguments -p or --password. Required minimum 8 chars."
        )
    else:
        password_encoded = password.encode("utf-8")
        salt = bcrypt.gensalt()
        password = bcrypt.hashpw(password_encoded, salt)

    if role == None or (role not in ["admin", "user"]):
        raise ValueError(
            "Invalid or empty Role. Arguments -r or --role. Valid role are admin and user."
        )

    # creating database connection
    conn = mysql.connector.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        port=DB_PORT,
    )

    # Get a cursor
    cursor = conn.cursor()

    # create user table if not exists
    create_user_table_query = create_user_table()
    cursor.execute(create_user_table_query)

    # creating user
    create_user_query = get_create_user_query()
    cursor.execute(
        create_user_query,
        (id, first_name, last_name, user_name, password, role, created_at),
    )
    conn.commit()

    # Closing connection
    cursor.close()
    conn.close()

    sys.stdout.write("User created successfully. \n")


if __name__ == "__main__":
    main()
