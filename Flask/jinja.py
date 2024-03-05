#Using JINJA
#creating variable and passing in template
#if statement
#for loop

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/blog")
def blog():
    library = [{'title': 'Technology', 'author': 'RK Sharma'},
               {'title': 'Book', 'author': 'BK Mittal'}]        
    return render_template("jinja.html", author = "Mathew", in_india = False, library = library)  


#Template inheritance

@app.route("/inherit")
def inherit():
    return render_template("temp_inheritance.html", greeting = 'Hello !!')


if __name__ == "__main__":
    app.run(debug=True)
