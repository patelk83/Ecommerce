from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_uploads  import IMAGES, UploadSet, configure_uploads, patch_request_class
import os

basedir=os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://{user}:{password}@{server}/{database}'.format(user='root', password='root123@pass', server='localhost', database='flaskdb')
app.config['SECRET_KEY'] = 'securesecretkey'
app.config['UPLOADED_PHOTOS_DEST'] =os.path.join(basedir,'static/images')

photos = UploadSet('photos', IMAGES)
configure_uploads(app,photos)
patch_request_class(app)

db = SQLAlchemy(app)
bcrypt= Bcrypt(app)



from .admin import routes

from shop.products import routes
from shop.carts import carts