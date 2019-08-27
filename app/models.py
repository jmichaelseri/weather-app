from app import db

class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), index=-True, unique=True)
    lat = db.Column(db.Integer)
    lon = db.Column(db.Integer)

    def __repr__(self):
        return '<City {}>'.format(self.name)
