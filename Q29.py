import psycopg2

conn = psycopg2.connect(host = "localhost", dbname = "mynewdb", user = "postgres", password = 'sfdc123*', port = 5432)
cur = conn.cursor()

cur.execute("create table if not exists student1 (id int primary key, name varchar(50), course varchar(20))")
cur.execute("""insert into student1
            values (1, 'Karan', 'MBA'),
            (2, 'Priya', 'MCA'),
            (3, 'Monica', 'Btech')""")

user_id = input("update info of Student with id : ")
user_in = input("What do you want to update(student name or course) : ")
input = input("Enter new value : ")


cur.execute(f"update student1 set {user_in} = '{input}' where id = {user_id}")

cur.execute("select * from student1")
print(cur.fetchall())


conn.commit()
cur.close()
conn.close()