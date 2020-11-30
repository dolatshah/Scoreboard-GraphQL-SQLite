from main import db


class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String)
    score = db.Column(db.Integer, default=0)
    age = db.Column(db.Integer)

    def to_dict(self):
        return {
            "id": self.id,
            "address": self.address,
            "score": self.score,
            "age": self.age
        }
