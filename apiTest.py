import os
from flask import Flask, request, jsonify, render_template
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)

app.config.from_object(os.environ["APP_SETTINGS"])
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

from models import User

@app.route("/")
def usersList():
    return "Hello"

@app.route("/add",methods=["GET", "POST"])
def add_user():
    name=request.args.get("name")
    age=request.args.get("age")
    occupation=request.args.get("occupation")
    # if name or age or occupation is None:
    #     return "Invalid request arguments. Use: /add?name=<name>&age=<age>&occupation=<occupation>"
    try:
        user = User(
            name=name,
            age=age,
            occupation=occupation
        )
        db.session.add(user)
        db.session.commit()
        return "User added. User id={}".format(user.id)
    except Exception as e:
        return(str(e))

@app.route("/getall")
def get_all():
    try:
        users = User.query.all()
        return jsonify([e.serialize() for e in users])
    except Exception as e:
        return(str(e))

@app.route("/get/<id_>")
def get_by_id(id_):
    try:
        user=User.query.filter_by(id=id_).first()
        return jsonify(user.serialize())
    except Exception as e:
        return(str(e))

@app.route("/add/form",methods=["GET", "POST"])
def add_user_form():
    if request.method == "POST":
        name=request.form.get("name")
        age=request.form.get("age")
        occupation=request.form.get("occupation")
        try:
            user = User(
                name=name,
                age=age,
                occupation=occupation
            )
            db.session.add(user)
            db.session.commit()
            return "User added. User id={}".format(user.id)
        except Exception as e:
            return(str(e))
    return render_template("getdata.html")

@app.route("/deleteall")
def delete_all_users():
    try:
        users = User.query.all()
        for user in users:
            db.session.delete(user)
        db.session.commit()
        return "Deleted all database entries."
    except Exception as e:
        return(str(e))

@app.route("/delete/<id_>")
def delete_by_id(id_):
    try:
        user = User.query.filter_by(id=id_).first()
        db.session.delete(user)
        db.session.commit()
        return "User deleted. User id={}".format(user.id)
    except Exception as e:
        return(str(e))


if __name__ == "__main__":
    app.run()
