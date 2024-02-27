import psycopg2

conn = psycopg2.connect(host = "localhost", dbname = "mynewdb", user = "postgres", password = 'sfdc123*', port = 5432)
cur = conn.cursor()

cur.execute("create table if not exists student (id int primary key, name varchar(50), course varchar(20))")
cur.execute("""insert into student
            values (1, 'Karan', 'MBA'),
            (2, 'Priya', 'MCA'),
            (3, 'Monica', 'Btech')""")

user_in = input("Want to search on what basis(course, name, id) : ")
in2 = input("Search Student : ")
if user_in != 'id':
    query1 = f"select * from student where {user_in} = '{in2}'" 
else:
    query1 = f"select * from student where {user_in} = {in2} "     

cur.execute(query1)
result = cur.fetchall()
print(result)

conn.commit()
cur.close()
conn.close()