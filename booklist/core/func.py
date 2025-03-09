import os
import mysql.connector
from typing import List, NamedTuple


class BookType(NamedTuple):
    id: str
    title: str
    summary: str
    ISBN: int
    genre: str
    publication_year: int
    author: str
    publisher: str
    rating: float


def list_books():
    """Return list of all available books."""

    query = """
        SELECT * FROM books;
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
    )
    books: List[BookType] = cursor.fetchall()

    # Closing connection
    cursor.close()
    conn.close()

    return books
