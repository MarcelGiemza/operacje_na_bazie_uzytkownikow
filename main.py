from flask import Flask

app = Flask(__name__)

users_db = [
    {"id": 1, "name": "Wojciech", "lastname": "Oczkowski"},
    {"id": 2, "name": "Marcel", "lastname": "Giemza"}
            ]

@app.get("/")
def home():
    return "Hello"

@app.get("/GET/users")
def get_all_users():
    return users_db

@app.get("/GET/users/<id>")
def get_user_by_id(id):
    return list(filter(lambda user: str(user["id"]) == id, users_db))[0]

if __name__ == "__main__":
    app.run("localhost", 3000)
