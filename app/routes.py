from flask import Flask


app = Flask(__name__)

@app.get("/")
def index():
    me = {
        "first_name": "Fernando",
        "last_name": "Iribe",
        "hobbies": "jiu-jitsu",
        "active": True
    }
    return me