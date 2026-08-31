import sqlite3


connection = sqlite3.connect("students.db")

cursor = connection.cursor()


cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        marks REAL
    )
""")


cursor.execute(
    """
    INSERT INTO students (name, age, marks)
    VALUES (?, ?, ?)
    """,
    ("Ghanshyam", 19, 95.5)
)


cursor.execute("SELECT * FROM students")

students = cursor.fetchall()

print("=== Students ===")

for student in students:
    print(student)


cursor.execute(
    """
    UPDATE students
    SET marks = ?
    WHERE name = ?
    """,
    (98.0, "Ghanshyam")
)


connection.commit()


connection.close()