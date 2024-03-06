from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:sfdc123*@localhost:5432/flask_db'

db = SQLAlchemy(app)

class Task(db.Model):
    __tablename__ = 'Task'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200), nullable=False)
    done = db.Column(db.Boolean, default=False)

    def __init__(self, title, done):
        self.title = title
        self.done = done

    def __repr__(self):
        return f"{self.id}. {self.title} = {self.done}"    

with app.app_context():
    db.create_all()

@app.route("/tasks")    #get method
def get_tasks():
    tasks = Task.query.all()
    task_list = [{'id': task.id, 'title': task.title, 'done': task.done} for task in tasks]  
    return jsonify({"tasks" : task_list}) 

@app.route("/tasks", methods=['POST'])
def create_task():
    data = request.get_json()
    new_task = Task(title= data['title'], done=data['done'])
    db.session.add(new_task)
    db.session.commit()
    return jsonify({'message': f'Task {new_task.title} created'})   

if __name__ == "__main__":
    app.run(debug=True)