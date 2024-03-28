from flask import Flask, render_template, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
import jwt
from functools import wraps
import bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:sfdc123*@localhost:5432/flask_db'
db = SQLAlchemy(app)

class User1(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	username = db.Column(db.String(100))
	email = db.Column(db.String(70), unique = True)
	password = db.Column(db.String(80))
	
with app.app_context():
    db.create_all()    

# decorator for verifying the JWT
def token_required(f):
	@wraps(f)
	def decorated(*args, **kwargs):
		token = request.args.get('token')
		
		if not token:
			return jsonify({'message' : 'Token is missing !!'})

		try:
			# decoding the payload to fetch the stored details
			data = jwt.decode(token, app.config['SECRET_KEY'])
		except:
			return jsonify({'message' : 'Token is invalid !!'}), 401
	return decorated

# User Database Route
# this route sends back list of users
@app.route('/user', methods =['GET'])
@token_required
def get_all_users(current_user):
	# querying the database for all the entries in it
	users = User1.query.all()
	# converting the query objects to list of jsons
	output = []
	for user in users:
		# appending the user data json to the response list
		output.append({'username' : user.username,
			           'email' : user.email})

	return jsonify({'users': output})

# route for logging user in
@app.route('/login', methods =['GET', 'POST'])
def login():
	if request.method == 'POST':
        # creates dictionary of form data
		auth = request.form
		user = User1.query.filter_by(email = auth.get('email')).first()
		if not user:
			return make_response("User does not exist !!")
		if bcrypt.checkpw(user.password.encode('utf-8'), auth.get('password').encode('utf-8')):		
            # generates the JWT Token
			token = jwt.encode({'id': user.id}, app.config['SECRET_KEY'])
			return make_response(jsonify({'token' : token.decode('UTF-8')}), 201)

		return make_response("Wrong Password !!")
	else:    
		return render_template("login.html")

# signup route
@app.route('/signup', methods =['GET', 'POST'])
def signup():
	if request.method == 'POST':
        # creates a dictionary of the form data
		data = request.form

        # gets name, email and password
		username, email = data.get('username'), data.get('email')
		password = data.get('password')

        # checking for existing user
		user = User1.query.filter_by(email = email).first()
		if not user:
			new_pass = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
			user = User1(username = username, email = email, password = new_pass)
			db.session.add(user)
			db.session.commit()
			return make_response('Successfully registered.', 201)
		else:
			return make_response('User already exists. Please Log in.')
	else:    
		return render_template("signup.html")

if __name__ == "__main__":
	app.run(debug = True)
