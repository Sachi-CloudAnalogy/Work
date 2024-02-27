#csv -- comma separated values
import psycopg2

conn = psycopg2.connect(host = 'localhost', user = 'postgres', dbname = 'mynewdb', password = 'sfdc123*', port = 5432)
cur = conn.cursor()
cur.execute("create table employee1(id int primary key, name varchar(50), location varchar(50), salary int, department varchar(50))")

f = open("csv.csv", "r")
while True:
    val = f.readline()
    if val == "":
        break
    else:
        cur.execute(f"insert into employee1(id, name, location, salary, department) values({val})")
    
f.close()
cur.execute("select * from employee1")
print(cur.fetchall())

conn.commit()
cur.close()
conn.close()