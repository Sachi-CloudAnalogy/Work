#basic flask program

from flask import Flask
app = Flask(__name__)     #object of flask class

@app.route("/")   #decorator
def func():
    return "Hello World !!"

if __name__ == "__main__":
    app.run()