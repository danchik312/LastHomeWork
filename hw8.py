import sqlite3
conn = sqlite3.connect('students.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Students (
                    id INTEGER PRIMARY KEY,
                    hobby TEXT,
                    first_name TEXT,
                    last_name TEXT,
                    birth_year INTEGER,
                    homework_score INTEGER
                )''')
students_data = [
    ('Reading', 'Azamat', 'Aitaliev', 1998, 15),
    ('Gaming', 'Alina', 'Zamirova', 1999, 8),
    ('Cooking', 'Gula', 'White', 2000, 12),
    ('Sports', 'Atabek', 'Black', 1997, 6),
    ('Music', 'Nurislam', 'Brown', 2001, 14),
    ('Painting', 'Islam', 'Green', 1996, 10),
    ('Writing', 'Daniel', 'Jack', 1995, 18),
    ('Dancing', 'Marina', 'Grey', 1994, 5),
    ('Traveling', 'Aziza', 'Blue', 1993, 13),
    ('Programming', 'Alik', 'Red', 1992, 9)
]
cursor.executemany('''INSERT INTO Students (hobby, first_name, last_name, birth_year, homework_score)
                      VALUES (?, ?, ?, ?, ?)''', students_data)
conn.commit()
cursor.execute('''SELECT * FROM Students WHERE LENGTH(last_name) > 10''')
print("Students with last names longer than 10 characters:")
print(cursor.fetchall())
cursor.execute('''UPDATE Students SET first_name = 'Genius' WHERE homework_score > 10''')
cursor.execute('''SELECT * FROM Students WHERE first_name = 'Genius' ''')
print("\nStudents with 'Genius' as first name after update:")
print(cursor.fetchall())
cursor.execute('''DELETE FROM Students WHERE id % 2 = 0''')
cursor.execute('''SELECT * FROM Students''')
print("\nAll students after deletion:")
print(cursor.fetchall())
conn.commit()
conn.close()