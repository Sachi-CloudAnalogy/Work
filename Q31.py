import psycopg2

conn = psycopg2.connect(host = 'localhost', user = 'postgres', dbname = 'mynewdb', password = 'sfdc123*', port = 5432)
cur = conn.cursor()

cur.execute("create table employee(id int primary key, name varchar(50), location varchar(50), salary int, department varchar(50))")
cur.execute("""insert into employee(id, name, location, salary, department)
            values(101, 'priya', 'Delhi', 30000, 'it'),
            (102, 'rahul', 'Jaipur', 20000, 'marketing'),
            (103, 'jasmine', 'Agra', 10000, 'finance'),
            (104, 'kriya', 'Delhi', 15000, 'it'),
            (105, 'raj', 'mumbai', 30000, 'finance')""")

average = "select avg(salary), department from employee group by department"
cur.execute(average)
print(cur.fetchall())

conn.commit()
cur.close()
conn.close()