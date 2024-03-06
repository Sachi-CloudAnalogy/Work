from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    
    if request.method == 'GET':
        return render_template("index.html")
    elif request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "cloud" and password == "123456":
            return "Successful"
        else:
            return "Failure"
        

if __name__ == "__main__":
    app.run(debug=True)
