from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import os #Resposável por buscar as variáveis de ambiente#
load_dotenv('.env')

app = Flask (__name__)
app.config['SQLALCHEMY_DATABASE_URI']= os.getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFIATIONS']=False
app.config['SECRET_KEY']= os.getenv('SECRET_KEY')
 
db=SQLAlchemy(app)
migrate=Migrate(app,db)
login_manager = LoginManager(app)
login_manager.login_view='login' #rota de login
bcrypt=Bcrypt(app)




from app.views import homepage

from app.models import Contato