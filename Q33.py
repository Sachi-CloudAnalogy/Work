import sqlite3

conn = sqlite3.connect('employees.db')   #create database
cur = conn.cursor()

query = """CREATE TABLE IF NOT EXISTS employees(
employee_id INT,
name TEXT,
department TEXT,
salary REAL );"""

cur.execute(query)

cur.execute("""INSERT INTO employees(employee_id, name, department, salary)
             VALUES(112, 'Vaibhav', 'IT', 40000)""")

conn.commit()

cur.execute("SELECT * FROM employees")
print(cur.fetchall())

cur.close()
conn.close()

print("Done")