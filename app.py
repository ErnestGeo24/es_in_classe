from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("post.html")

@app.route("/login", methods = ["POST"])
def login():
    user = request.form["user"]
    password = request.form["password"]
    if user == "admin" and password == "xxx123##":
        return render_template("login.html", user = user, password = password)
    else:
        return render_template("nonlogin.html")

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)