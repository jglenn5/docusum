import sqlite3

connection = sqlite3.connect("docusum.db")
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS documents (
        document_id INTEGER PRIMARY KEY AUTOINCREMENT,
        filename TEXT NOT NULL,
        summary_text TEXT,
        user_id INTEGER NOT NULL,
        created_at TEXT NOT NULL
    )
""")

connection.commit()
connection.close()