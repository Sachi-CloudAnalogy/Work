from flask import Flask, render_template
app = Flask(__name__)

@app.route("/template")
def template():
    return render_template("first.html")

if __name__ == "__main__":
    app.run()