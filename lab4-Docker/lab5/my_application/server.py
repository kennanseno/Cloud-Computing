from flask import Flask
app = Flask(__name__)

@app.route("/index")
def index():
	return "Index File"

@app.route("/hello")
def hello():
    return "Hello World!"

@app.route("/user/<user>")
def show_user_profile(user):
	return "Hello %s, " % user

@app.route("/post/<int:post_id>")
def show_pos(post_id):
	return "Post %d " % post_id 


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080,debug=True)
