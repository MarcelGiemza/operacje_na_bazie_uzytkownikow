from flask import Flask, Response, request

app = Flask(__name__)

CREATED = 201
OK = 200
CREATE_WRONG_REQUEST = 400

users_db = [
    {"id": 1, "name": "Wojciech", "lastname": "Oczkowski"},
    {"id": 2, "name": "Marcel", "lastname": "Giemza"}
            ]

def get_user_by_id(id):
    user = list(filter(lambda user: str(user["id"]) == id, users_db))
    if len(user) == 0:
        return {}
    return user[0]

def create_user(id, name, lastname):
    pass

@app.get("/")
def home():
    return "Hello"

@app.get("/ping")
def ping():
    return "ping"

@app.route("/users", methods = ["GET", "POST"])
def users():
    if request.method == "GET":
        return users_db
    if request.method == "POST":
        data = request.get_json()
        data_keys = tuple(data.keys())
        if len(data_keys) == 2\
                and data_keys.count("name") == 1\
                and data_keys.count("lastname") == 1:
            user_ids = [user["id"] for user in users_db]
            users_db.append({
                "id": max(user_ids)+1,
                "name": data["name"],
                "lastname": data["lastname"],
            })
            return Response(status=CREATED)
        return Response(status=CREATE_WRONG_REQUEST)

@app.route("/users/<id>", methods = ["GET"])
def users_id(id):
    if request.method == "GET":
        return get_user_by_id(id)


 
if __name__ == "__main__": 
    app.run("localhost", 3000)
