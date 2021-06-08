from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField
from wtforms.validators import InputRequired, Optional, Email

class AddCupcakeForm(FlaskForm):

    flavor = SelectField("Flavor", choices=[('chocolate','Chocolate'), ('vanilla', 'Vanilla'),('mega_burst','Mega Burst')]))
    size = StringField("Size")
    rating = IntegerField("Rating")
    image = StringField("Image")
    #category = RadioField("Category", choices=[('ic','Ice Cream'), ('chips', 'Potato Chips'),('candy','Candy/Sweets')])
