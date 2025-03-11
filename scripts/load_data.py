"""Standalone script to load data to sqldb."""

import os
import sys
import json
import mysql.connector


def create_book_query():
    query = """
        CREATE TABLE
            IF NOT EXISTS books (
                id VARCHAR(36) PRIMARY KEY,
                title VARCHAR(255) UNIQUE,
                summary TEXT,
                ISBN BIGINT UNSIGNED,
                genre VARCHAR(255),
                publication_year INT UNSIGNED,
                author VARCHAR(255),
                publisher VARCHAR(255) NULL,
                rating FLOAT
            )
    """

    return query

def insert_books_query():
    query = """
        INSERT INTO
            books (
                id,
                title,
                summary,
                ISBN,
                genre,
                publication_year,
                author,
                publisher,
                rating
            )
        VALUES
            (
                "e8c7c561-bc25-46f2-8b27-5ea8d42a9c5e",
                "Harry Potter and the Sorcerer's Stone",
                "Harry Potter, an orphan living with his cruel Muggle (non-magical) relatives, discovers that he is a wizard. He begins attending Hogwarts School of Witchcraft and Wizardry, where he makes friends with Ron Weasley and Hermione Granger. Together, they embark on a journey to uncover the truth about the Sorcerer's Stone, a powerful object that can grant eternal life.",
                9780439554930,
                "Fantasy, Magic",
                1997,
                "J.K. Rowling",
                "Scholastic",
                4.4
            ),
            (
                "26e3e8a8-a882-4a97-b06a-48c4b2f7eac6",
                "To Kill a Mockingbird",
                "Set in the Deep South during the 1930s, this Pulitzer Prize-winning novel follows a young girl's experience of racial injustice in a small Alabama town. As she witnesses her father, a lawyer, defend a wrongly accused black man, she learns valuable lessons about prejudice, empathy, and understanding.",
                9780061120084,
                "Fiction, Classics",
                1960,
                "Harper Lee",
                "J.B. Lippincott & Co.",
                4.7
            ),
            (
                "b6a7c3b6-2398-49c1-a6c0-4ee7a5e7bfc0",
                "The Invisible Man",
                "This masterpiece of science fiction is the fascinating story of Griffin, a scientist who creates a serum to render himself invisible, and his descent into madness that follows.",
                9780486284728,
                "Science Fiction, Classics",
                1897,
                "H.G. Wells",
                "Pearson's Magazine",
                4.1
            ),
            (
                "7bab5cff-6b86-4027-891e-b41441261b9e",
                "The Nightingale",
                "Set in France during World War II, this historical fiction novel tells the story of two sisters, Vianne and Isabelle, as they navigate the difficulties and dangers of living under German occupation. While Vianne tries to maintain a sense of normalcy and protect her young daughter, Isabelle joins the French Resistance, risking everything to fight against the Nazis.",
                9781250066197,
                "Historical Fiction, War",
                2015,
                "Kristin Hannah",
                "St. Martin's Press",
                4.8
            ),
            (
                "f2541876-7025-4bb1-ac7c-e30f664ed919",
                "The Hitchhiker's Guide to the Galaxy",
                "When Earth is destroyed to make way for a hyperspace bypass, unwitting human Arthur Dent hitches a ride on a passing spaceship. He embarks on a misadventure-filled journey through space and time, accompanied by his friend Ford Prefect, an alien researching Earth for the titular guidebook.",
                9781400052929,
                "Science Fiction, Comedy",
                1979,
                "Douglas Adams",
                "Pan Books",
                4.4
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

    # create book table
    book_table_query = create_book_query()
    cursor.execute(book_table_query)

    sys.stdout.write("Creating Book Table \n")

    # inserting book data
    books_data = insert_books_query()
    cursor.execute(books_data)

    sys.stdout.write("Inserting Book Data \n")
    
    conn.commit()

    # Closing connection
    cursor.close()
    conn.close()


if __name__ == "__main__":
    main()
