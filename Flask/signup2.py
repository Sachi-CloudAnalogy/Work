# form validation

from flask import Flask, render_template, redirect, url_for
from forms import SignUpForm    #from forms.py

app = Flask(__name__)
app.config["SECRET_KEY"] = "key123"       #secret key

@app.route("/signup2", methods=['GET','POST'])
def signup():                 #creating signup form

    form = SignUpForm()

    if form.validate_on_submit():                  #validating form
        username = form.username.data
        password = form.password.data
        id =  form.id.data
        gender = form.id.data
        indian = form.indian.data
        remarks = form.remarks.data
        result = {"Username" : username, "password" : password, "id" : id, "gender" : gender, 
                  "indian" : indian, "remarks" : remarks}
        return redirect(url_for("result"))
    
    return render_template("signup.html", form = form)


if __name__ == "__main__":
    app.run(debug=True)


# signup.html, user.html, forms.py and signup2.py  --- are part of same program