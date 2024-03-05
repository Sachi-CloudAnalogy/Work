from flask import Flask, render_template, request
from forms import SignUpForm    #from forms.py

app = Flask(__name__)
app.config["SECRET_KEY"] = "key123"       #secret key

@app.route("/signup", methods=['GET','POST'])
def signup():                 #creating signup form
    form = SignUpForm()
    if form.is_submitted():
        result = request.form
        return render_template('user.html', result=result)
    return render_template("signup.html", form = form)

if __name__ == "__main__":
    app.run(debug=True)