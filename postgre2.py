import psycopg2

hostname = "localhost"
db = "postgres"
username = "postgres"
port_id = 5432
pwd = "sfdc123*"

conn = psycopg2.connect(host = hostname, dbname = db, user = username, port = port_id, password = pwd)
cur = conn.cursor()

cur.execute("drop table if exists customer;")

cur.execute("""create table if not exists customer(
            id int primary key,
            name varchar(50),
            bill int,
            product varchar(100));""")

cur.execute("""insert into customer
            values(101, 'Joe', 4000, 'Laptop'),
            (202, 'Kim', 2000, 'earphones'),
            (303, 'Ronnie', 5000, 'Keyboard');""")

cur.execute("select * from customer;")
print(cur.fetchall())

cur.execute("update customer set product = 'speakers' where name = 'Ronnie';")
cur.execute("select * from customer;")
print(cur.fetchall())

cur.execute("delete from customer where bill = 2000;")
cur.execute("select * from customer;")
print(cur.fetchall())

cur.execute("alter table customer add column date int;")
cur.execute("select * from customer;")
print(cur.fetchall())

cur.execute("select max(bill) from customer;")
print(cur.fetchone())

cur.execute("select avg(bill) from customer;")
print(cur.fetchone())

conn.commit()
cur.close()
conn.close()