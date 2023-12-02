from flask import Flask 
from flask_sqlalchemy import SQLAlchemy  # instalar:  pip install -U Flask-SQLAlchemy
from flask_marshmallow import Marshmallow   #instalar : pip install flask-marshmallow
from flask_cors import CORS   # pip install -U flask-cors

app=Flask(__name__)   #creamos el objeto app
CORS(app)     # soluciona el error cuando el frontend accede a los endpoint que genera el backend

app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:root@localhost/lacocinadejuan'
#MarcelaCerda:Lastra4259@MarcelaCerda.mysql.pythonanywhere-services.com/MarcelaCera$proyecto'
#                                                           usuario:clave@localhost/nombreBaseDeDAtos
                                                           
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db= SQLAlchemy(app)
ma=Marshmallow(app)


from controladores.producto_controlador import *
from controladores.subtipo_controlador import *

         
# ejecutaria el servidor Flask *******************************
if __name__=='__main__':  
    app.run(debug=True, port=5000)    # ejecuta el servidor Flask en el puerto 5000
   
