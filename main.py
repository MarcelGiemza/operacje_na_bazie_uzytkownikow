from flask import Flask, Response, request

app = Flask(__name__)

OK = 200
CREATED = 201
NO_CONTENT = 204
WRONG_REQUEST = 400

users_db = {
    "1": {"name": "Wojciech", "lastname": "Oczkowski"},
    "2": {"name": "Marcel", "lastname": "Giemza"}
            }


def update_users(id, name, lastname):
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
    match request.method:
        case "GET":
            return {"users": [{
                "id": user[0],
                "name": user[1]["name"],
                "lastname": user[1]["lastname"],
            } for user in users_db.items()]}
        case "POST":
            data = request.get_json()
            data_keys = tuple(data.keys())
            if len(data_keys) == 2\
                    and data_keys.count("name") == 1\
                    and data_keys.count("lastname") == 1:
                user_ids = [int(id) for id in users_db.keys()]
                update_users(str(max(user_ids)+1), data["name"], data["lastname"])
                return Response(status=CREATED)
            return Response(status=WRONG_REQUEST)

@app.route("/users/<id>", methods = ["GET", "PATCH", "PUT", "DELETE"])
def users_id(id):
    match request.method:
        case "GET":
            return users_db[id]
        case "PATCH":
            user = users_db.get(id, False)
            data = request.get_json()
            data_keys = tuple(data.keys())
            if user and len(data_keys) == 1:
                if data_keys.count("name") == 1:
                    update_users(id, data["name"], user["lastname"])
                    return Response(status=NO_CONTENT)
                if data_keys.count("lastname") == 1:
                    update_users(id, user["name"], data["lastname"])
                    return Response(status=NO_CONTENT)
            return Response(status=WRONG_REQUEST)
        case "PUT":
            user = users_db.get(id, False)
            data = request.get_json()
            data_keys = tuple(data.keys())
            if user and len(data_keys):
                if len(data_keys) == 2\
                        and data_keys.count("name") == 1\
                        and data_keys.count("lastname") == 1:
                    update_users(id, data["name"], data["lastname"])
                    return Response(status=NO_CONTENT)
            return Response(status=WRONG_REQUEST)
        case "DELETE":
            user = users_db.get(id, False)
            if user:
                users_db.pop(id)
                return Response(status=NO_CONTENT)
            return Response(status=WRONG_REQUEST)


if __name__ == "__main__": 
    app.run("localhost", 3000)
