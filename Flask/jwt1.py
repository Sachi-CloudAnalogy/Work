from flask import Flask
import jwt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

@app.route("/user/<email>", methods=['GET', 'POST'])
def code(email):
    token = jwt.encode({'email': email}, 'secret', algorithm="HS256")
    return f"{token}"
    # data = jwt.decode(token, 'secret', algorithm="HS256")
    # return data
    #return jsonify({'token': token.decode('utf-8')})

if __name__ == "__main__":
    app.run(debug=True)
