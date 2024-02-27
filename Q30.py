import psycopg2

conn = psycopg2.connect(host = 'localhost', user = 'postgres', dbname = 'mynewdb', password = 'sfdc123*', port = 5432)
cur = conn.cursor()

cur.execute("create table salaries(id int primary key, location varchar(50), salary int)")
cur.execute("""insert into salaries
            values(101, 'Delhi', 30000),
            (102, 'Jaipur', 20000),
            (103, 'Agra', 10000),
            (104, 'Delhi', 15000)""")
cur.execute("select max(salary) from salaries")
max = cur.fetchall()
cur.execute("select min(salary) from salaries")
min = cur.fetchall()

print("Max salary = ",max)
print("Min salary = ",min)

conn.commit()
cur.close()
conn.close()