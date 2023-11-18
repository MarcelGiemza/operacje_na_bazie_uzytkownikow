from flask import Flask, Response, request

app = Flask(__name__)

CREATED = 201
OK = 200
CREATE_WRONG_REQUEST = 400

users_db = {
    "1": {"name": "Wojciech", "lastname": "Oczkowski"},
    "2": {"name": "Marcel", "lastname": "Giemza"}
            }


def create_user(id, name, lastname):
            users_db.update({
                id: {
                "name": name,
                "lastname": lastname}
            })
    

@app.get("/")
def home():
    return "Hello"

@app.get("/ping")
def ping():
    return "ping"

@app.route("/users", methods = ["GET", "POST"])
def users():
    if request.method == "GET":
        return {"users": [{
            "id": user[0],
            "name": user[1]["name"],
            "lastname": user[1]["lastname"],
        } for user in users_db.items()]}
    if request.method == "POST":
        data = request.get_json()
        data_keys = tuple(data.keys())
        if len(data_keys) == 2\
                and data_keys.count("name") == 1\
                and data_keys.count("lastname") == 1:
            user_ids = [int(id) for id in users_db.keys()]
            create_user(str(max(user_ids)+1), data["name"], data["lastname"])
            return Response(status=CREATED)
        return Response(status=CREATE_WRONG_REQUEST)

@app.route("/users/<id>", methods = ["GET"])
def users_id(id):
    if request.method == "GET":
        return users_db[id]


 
if __name__ == "__main__": 
    app.run("localhost", 3000)
