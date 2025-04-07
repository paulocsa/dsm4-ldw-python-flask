# importando a classe resource do flask-restful

from flask_restful import Resource
from api import api


class MovieList(Resource):
    def get(self):
        return "Olá mundo! API rodando"


class RecursosAPI(Resource):
    def get(self):
        return "GET Recursos API"

    def post(self):
        return "POST Recursos API"

    def put(self):
        return "PUT Recursos API"

    def delete(self):
        return "DELETE Recursos API"



api.add_resource(MovieList, '/movies')
api.add_resource(RecursosAPI, '/recursos')

