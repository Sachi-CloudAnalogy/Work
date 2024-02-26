#python script to connect to database
import psycopg2

hostname = "localhost"
db = "postgres"
username = "postgres"
port_id = 5432
pwd = "sfdc123*"
cur = None
conn = None

#form connection
#to avoid error use try and except block
try:
    conn = psycopg2.connect(host = hostname, dbname = db, user = username, port = port_id, password = pwd)

    #create cursor
    cur = conn.cursor()
    
    cur.execute("DROP TABLE IF EXISTS employee")
    #execute cursor
    query1 = """CREATE TABLE IF NOT EXISTS employee(             
                id int PRIMARY KEY,
                name varchar(50),
                salary int);"""
    cur.execute(query1)          #CREATE

    q2 = "INSERT INTO employee(id, name, salary) VALUES(11, 'Garry', 20000);"
    cur.execute(q2)              #INSERT

    cur.execute("INSERT INTO employee VALUES(22, 'Rose', 22000);")

    q3 = "UPDATE employee SET id = 44 WHERE name = 'Rose';"
    cur.execute(q3)              #UPDATE

    q4 = "DELETE FROM employee WHERE name = %s"
    name = ("Garry",)
    cur.execute(q4, name)        #DELETE

    cur.execute("SELECT * FROM employee")
    print(cur.fetchall())        #READ

    #commit transaction
    conn.commit()
except Exception as error:
    print(error)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()        