from models import db, Cupcake
from app import app

# create all tables and seed them
db.drop_all()
db.create_all()

c1 = Cupcake(flavor="Chocolate", size="Medium", rating=3)
c2 = Cupcake(flavor="Vanilla", size="Small", rating=3)
c3 = Cupcake(flavor="Mega Burst", size="Large", rating=5)

db.session.add(c1)
db.session.add(c2)
db.session.add(c3)

db.session.commit()
