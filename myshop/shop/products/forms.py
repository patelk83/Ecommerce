from flask_wtf.file import FileAllowed, FileField, FileRequired
from flask_wtf import FlaskForm
from wtforms import Form, IntegerField,StringField,BooleanField, TextAreaField, validators, IntegerField, DecimalField
class Addproducts(Form):
    name = StringField("Name",[validators.DataRequired()])
    price= DecimalField("Price",[validators.DataRequired()])
    discount= IntegerField("Discount",default=0)
    stock= IntegerField("Stock",[validators.DataRequired()])
    description = TextAreaField("Description",[validators.DataRequired()])
    colors= TextAreaField("Color",[validators.DataRequired()])

    image_1 = FileField('Image 1',validators=[FileAllowed(['jpg', 'png'], 'Images only!')])
    image_2 = FileField('Image 2', validators=[FileAllowed(['jpg', 'png'], 'Images only!')])
    image_3 = FileField('Image 3', validators=[ FileAllowed(['jpg', 'png'], 'Images only!')])