#URL parameter handling

from flask import Flask, request
app = Flask(__name__)

@app.route("/<name>", methods = ["GET", "POST"])
def hi(name):
    return f"Hi {name} !!!!!"

@app.route("/handle_parameter")
def handle():
    return str(request.args)           #return empty dictionary

@app.route("/handle")
def handle2():
    day = request.args.get("day")
    date = request.args["date"]
    return f"{day}, {date}"

@app.route("/hello", methods = ["GET", "POST"])
def hello():
    if request.method == "GET":
        return "GET method \n"
    elif request.method == "POST":
        return "POST method \n"


if __name__ =="__main__":
    app.run()