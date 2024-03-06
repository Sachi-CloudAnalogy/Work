#basic flask program

from flask import Flask
app = Flask(__name__)     #object of flask class

@app.route("/")   #decorator
def func():
    return "Hello World !!"

# if __name__ == "__main__":
#     app.run()                              with this--- python3 app.py

# without app.run(), run it like this
# export FLASK_APP=app.py
# export FLASK_ENV=development
# flask run