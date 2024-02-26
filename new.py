import psycopg2

conn = psycopg2.connect(host = "localhost", dbname = "mynewdb", user = "postgres", password = 'sfdc123*', port = 5432)
cur = conn.cursor()

cur.execute("DROP TABLE company;")

cur.execute("CREATE TABLE IF NOT EXISTS company(email VARCHAR(50), name VARCHAR(50));")

cur.execute("""INSERT INTO company(email, name)
             VALUES('abs@gmail.com', 'john'),
             ('xyz@gmail.com', 'priya');""")

cur.execute("ALTER TABLE company ADD COLUMN id int;")

cur.execute("SELECT * FROM company;")
print(cur.fetchall())

cur.execute("INSERT INTO company VALUES('123@gmail.com','Rahul', 101);")
cur.execute("SELECT * FROM company;")
print(cur.fetchall())

cur.execute("INSERT INTO company VALUES('arshad@gmail.com', 'Radha', 102);")

#check if same email exist
user_id = "xyz@gmail.com"
cur.execute(f"SELECT email FROM company where email = '{user_id}'")
user = cur.fetchall()[0][0]
print(user)
if user_id == user:
    print("Same email")
         

conn.commit()
cur.close()
conn.close()