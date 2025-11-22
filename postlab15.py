import sqlite3

conn = sqlite3.connect('student_record.db')
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS student_record")

cursor.execute('''
CREATE TABLE IF NOT EXISTS student_record (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Enrollment INTEGER NOT NULL,
    name TEXT NOT NULL,
    Subject TEXT NOT NULL,
    Mark INTEGER NOT NULL
)
''')
conn.commit()

enrollment = int(input("Enter Enrollment Number: "))
name = input("Enter Student Name: ")

subjects = input("Enter Subjects (comma separated): ").split(",")
marks = input("Enter Marks for each subject (comma separated): ").split(",")

subjects = [s.strip() for s in subjects]
marks = [int(m.strip()) for m in marks]

student_records = [(enrollment, name, subjects[i], marks[i]) for i in range(len(subjects))]

cursor.executemany('''
INSERT INTO student_record (Enrollment, name, Subject, Mark)
VALUES (?, ?, ?, ?)
''', student_records)

conn.commit()

print("\nStudent enrolled in multiple subjects successfully!\n")

cursor.execute("SELECT * FROM student_record")
rows = cursor.fetchall()

print("All Student Records:")
for row in rows:
    print(row)

cursor.execute('SELECT name, Subject, Mark FROM student_record WHERE Mark > 90')
high_marks = cursor.fetchall()

print("\nStudents scoring above 90:")
for h in high_marks:
    print(h)

cursor.execute('''
UPDATE student_record 
SET Mark = 98 
WHERE name = 'ASHUTOSH KUMAR SINGH' AND Subject = 'PWP'
''')
conn.commit()

cursor.execute('''
SELECT name, Mark FROM student_record 
WHERE name='ASHUTOSH KUMAR SINGH' AND Subject='PWP'
''')
updated = cursor.fetchone()
if updated:
    print(f"\nUpdated Mark: {updated}")

cursor.execute('''
DELETE FROM student_record 
WHERE name = 'DEVENDRASINH DOLATSINH JADEJA'
''')
conn.commit()

cursor.execute('''
SELECT * FROM student_record 
WHERE name='DEVENDRASINH DOLATSINH JADEJA'
''')
deleted = cursor.fetchone()

if deleted is None:
    print("\nRecord deleted successfully.")

cursor.execute('SELECT AVG(Mark) FROM student_record')
avg_mark = cursor.fetchone()[0]
print(f"\nAverage Marks: {avg_mark:.2f}")
conn.close()
