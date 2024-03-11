from flask import Flask, jsonify
import jwt
from datetime import datetime, timedelta

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

@app.route("/user/<email>")
def code(email):
    token = jwt.encode({'email': email, 'expire': str(datetime.utcnow()+ timedelta(seconds=120))}, 
                       app.config['SECRET_KEY'])
    
    return jsonify({'token': token})

if __name__ == "__main__":
    app.run(debug=True)

   