import os

import psycopg
from flask import Flask

app = Flask(__name__)


def get_db_connection():
    return psycopg.connect(
        host=os.getenv("DB_HOST", "localhost"),
        port=os.getenv("DB_PORT", "5432"),
        dbname=os.getenv("DB_NAME", "devopsdb"),
        user=os.getenv("DB_USER", "devopsuser"),
        password=os.getenv("DB_PASSWORD", "devopspass"),
    )


@app.route("/")
def home():
    return {"message": "Hello DevOps"}


@app.route("/db")
def database_test():
    try:
        with get_db_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT 1")
                result = cursor.fetchone()

        return {"database": "connected", "result": result[0]}

    except Exception as e:
        return {"database": "connection failed", "error": str(e)}, 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
