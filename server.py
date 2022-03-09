from flask import Flask, render_template, request, redirect
from user import User

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/users")
def users():
    users = User.get_all()
    tamaño = len(users)
    return render_template('leer.html', all_friends = users, tamañoBase = tamaño)

@app.route("/users/new")
def usersNew():
    return render_template('crear.html')

@app.route('/create_user', methods=["POST"])
def create_user():
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }
    User.save(data)
    return redirect('/users')
            
if __name__ == "__main__":
    app.run(debug=True)