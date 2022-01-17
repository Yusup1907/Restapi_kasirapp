from app import db

class Categories(db.Model):
    id = db.Column(db.BigInteger, primary_key=True,  autoincrement=True)
    name = db.Column(db.String(250), nullable=False)


    def __repr__(self):
        return '<Categories {}>'.format(self.name)