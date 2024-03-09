from flask import Flask, url_for, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy 
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
import bcrypt       #for password hashing

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:sfdc123*@localhost:5432/flask_db'
app.config['SECRET_KEY'] = 'secret'
db = SQLAlchemy(app)

login_manager = LoginManager()     #help in logging in
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"({self.id}) {self.username} -- {self.password}"

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        if bcrypt.checkpw(password, existing_user.password):
            login_user(existing_user)
            return redirect(url_for("dashboard"))

    return render_template("login.html")

@app.route("/register", methods=['GET', 'POST'])
def register():
    username = request.form.get("username")
    password = request.form.get("password")
    existing = User.query.filter_by(username=username).first()
    if existing:
        raise Exception("Username already exist !!")
    else:
        new_pass = bcrypt.hashpw(password, bcrypt.gensalt())             #hashing the password
        new_user = User(username=username, password=new_pass)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("login"))
    return render_template("register.html")

@app.route("/dashboard", methods=['GET', 'POST'])
@login_required
def dashboard():
    return render_template("dashboard.html")

@app.route("/logout", methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)


# login.html, home.html, register.html, dashboard.html  & autheticate.py are part of same program.