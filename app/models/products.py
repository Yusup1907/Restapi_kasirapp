from app import db
from app.models.categories import Categories

class Products(db.Model):
    id = db.Column(db.BigInteger, primary_key=True,  autoincrement=True)
    kode = db.Column(db.String(5), nullable=False)
    name = db.Column(db.String(250), nullable=False)
    harga = db.Column(db.Integer)
    category = db.Column(db.BigInteger, db.ForeignKey(Categories.id))


    def __repr__(self):
        return '<Products {}>'.format(self.name)