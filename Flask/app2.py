from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "HELLO !!!!"

# Pass the required route to the decorator. 
@app.route("/hi")
def hi():
    return "HI !!!"

@app.route("/user/<username>")    #passing variable in url
def user(username):
    return f"hello, {username} !!"

@app.route('/post/<int:id>')   #specify datatype of variable
def show_post(id): 
    return f'This post has the id {id}'

if __name__ == "__main__":
    app.run()    
  
