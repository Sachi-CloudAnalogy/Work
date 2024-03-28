from flask import Flask, jsonify
import jwt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

@app.route("/user/<email>")
def code(email):
    token = jwt.encode({'email': email}, app.config['SECRET_KEY'], algorithm = 'HS256')
    
    return jsonify({'token': token})

if __name__ == "__main__":
    app.run(debug=True)

   