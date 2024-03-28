from flask import Flask, request, jsonify, make_response, render_template, session
import jwt
from functools import wraps

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

def token_required(func):
    @wraps(func)
    def decorated (*args, **kwargs):
        token = request.args.get('token')
        if not token:
            return jsonify({'Alert': 'Token is missing'})
        try:
            payload = jwt.decode(token, "secret", algorithms=['HS256'])
        except:
            return jsonify({'Alert': 'Invalid Token !!'})
        return decorated

# @app.route('/public')
# def public():
#     return "For public"

# @app.route('/auth')
# @token_required
# def auth():
#     return "JWT is verified. Welcome to your dashboard."        

@app.route("/")
def home():
    if not session.get("logged_in"):
        return render_template("login.html")
    else:
        return "Logged in currently !!"
    
@app.route("/login", methods=['POST'])
def login():
    if request.form['username'] and request.form['password'] == '123456':
        session['logged_in'] = True
        token = jwt.encode({'user': request.form['username']}, "secret", algorithm='HS256')
        return jsonify({'token': token})
    else:
        return make_response('Unable to verify !!', 403, {'WWW-Authenticate': 'Basic realm : "Authentication Failed!"'})

if __name__ == "__main__":
    app.run(debug=True)    
