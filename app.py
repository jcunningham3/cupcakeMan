from flask import Flask, render_template, request, session, flash, redirect, jsonify
from models import db, connect_db, Cupcake


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

@app.route('/')
def homepage():
    cupcakes = Cupcake.query.all()
    return render_template('home.html', cupcakes=cupcakes)



# API ROUTES -------------------------------------------------------------------

@app.route('/api/cupcakes')
# get data about all cupcakes
def list_cupcakes():
    all_cupcakes = [cupcake.serialized() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes=all_cupcakes)

@app.route('/api/cupcakes/<int:id>')
# list a single cupcake
def get_cupcakes(id):
    cupcake = Cupcake.query.get_or_404(id)
    return jsonify(cupcake=cupcake.serialized())

@app.route('/api/cupcakes', methods=["POST"])
def create_cupcake():
    # create a new cupcake
    new_cupcake = Cupcake(flavor=request.json['flavor'], size=request.json['size'], rating=request.json['rating'], image=request.json['image'] or None)
    db.session.add(new_cupcake)
    db.session.commit()
    return (jsonify(cupcake=new_cupcake.serialized()), 201)

@app.route('/api/cupcakes/<int:id>', methods=["PATCH"])
def update_cupcake(id):
    # update a cupcake
    cupcake = Cupcake.query.get_or_404(id)
    request.json
    cupcake.flavor = request.json.get['flavor', cupcake.flavor]
    cupcake.size = request.json.get['size', cupcake.size]
    cupcake.rating = request.json.get['rating', cupcake.rating]
    cupcake.image = request.json.get['image', cupcake.image]
    db.session.commit()
    return jsonify(cupcake=cupcake.serialized())

@app.route('/api/cupcakes/<int:id>', methods=["DELETE"])
# delete a cupcake
def delete_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(message="deleted")
