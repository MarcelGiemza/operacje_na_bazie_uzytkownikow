from flask import Flask, request

app = Flask(__name__)

users_db = [
    {"id": 1, "name": "Wojciech", "lastname": "Oczkowski"},
    {"id": 2, "name": "Marcel", "lastname": "Giemza"}
            ]

def get_user_by_id(id):
    user = list(filter(lambda user: str(user["id"]) == id, users_db))
    if len(user) == 0:
        return {}
    return user[0]

@app.get("/")
def home():
    return "Hello"

@app.get("/ping")
def ping():
    return "ping"

@app.route("/users/", methods = ["GET", "POST"])
def users():
    if request.method == "GET":
        return users_db
    if request.method == "POST":
        pass

@app.route("/users/<id>", methods = ["GET"])
def users_id(id):
    if request.method == "GET":
        return get_user_by_id(id)



if __name__ == "__main__":
    app.run("localhost", 3000)
