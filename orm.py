from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
class Person(Base):
    __tablename__ = "people"
    id = Column("id", Integer, primary_key=True)
    name = Column("name", String)
    city = Column("city", String)

    def __init__(self, id, name, city):
        self.id = id
        self.name = name
        self.city = city

    def __repr__(self):
        return f"({self.id}) {self.name} from {self.city}"

engine = create_engine("postgresql+psycopg2://postgres:sfdc123*@localhost:5432/newdb", echo=True)      
Base.metadata.create_all(bind = engine)
Session = sessionmaker(bind = engine)
session = Session()

p1 = Person(123, 'Priya', 'Delhi')
p2 = Person(234, 'Karan', 'Mumbai')
session.add(p1)
session.add(p2)
session.commit()

result = session.query(Person).all()
print(result)

r1 = session.query(Person).filter(Person.city == 'Delhi')
print(r1)

class Thing(Base):
    __tablename__ = "things"
    tid = Column("tid", Integer, primary_key=True)
    description = Column("description", String)
    owner = Column("owner", Integer, ForeignKey("people.id"))

    def __init__(self, tid, desc, owner):
        self.tid = tid
        self.description = desc
        self.owner = owner

    def __repr__(self):
        return f"({self.tid}) {self.description} owned by{self.owner}"

t1 = Thing(12, 'car', p1.id)
t2 = Thing(23, 'laptop', p2.id)
session.add(t1)
session.add(t1)
session.commit()

r2 = session.query(Thing, Person).filter(Thing.owner == Person.id).filter(Person.name == 'Priya').all()
print(r2)