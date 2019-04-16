from apiTest import db

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    age = db.Column(db.Integer())
    occupation = db.Column(db.String())

    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation

    def __repr__(self):
        return "<id {}>".format(self.id)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "occupation": self.occupation
        }