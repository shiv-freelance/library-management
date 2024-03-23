from mysql.connector import connect

# host, user, password, port, database


def get_connection():
    return connect(
        host="localhost", user="root", password="Aug2023", database="movie_db"
    )
