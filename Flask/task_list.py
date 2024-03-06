# creating a task list
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:sfdc123*@localhost:5432/flask_db'

db = SQLAlchemy(app)

class Task(db.Model):
    __tablename__ = 'Task'
    sno = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    done = db.Column(db.String(50), default=False)

    def __repr__(self):
        return f"{self.sno}. {self.title} = {self.done}" 
    
with app.app_context():
    db.create_all()


@app.route("/", methods=['GET', 'POST'])
def task():
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']
        done = request.form['done']
        new_task = Task(title=title, desc=desc, done=done)
        db.session.add(new_task)
        db.session.commit()

    task_list = Task.query.all()
    return render_template("list.html", task_list=task_list)

@app.route("/show")
def show():
    tasks = Task.query.all()
    print(tasks)
    return "all records are shown on the terminal"

if __name__ == "__main__":
    app.run(debug=True)
