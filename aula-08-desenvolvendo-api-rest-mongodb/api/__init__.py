# importação das ferramentas para montar o site ou aplicação

# flask
from flask import Flask

# flask restful
from flask_restful import Api

# importando pymongo
from flask_pymongo import PyMongo

# carregando o flask men, chamando ele de app
app = Flask(__name__)

# configurando o flask com o mongoDB
app.config["MONGO_URI"] = 'mongodb://localhost:27017/api-movies'
# criando a API restful em cima do app flask
api = Api(app)

# carregando o pymongo
mongo = PyMongo(app)

# importando os recursos
from .resources import movies_resources
