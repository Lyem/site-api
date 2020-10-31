import os
from datetime import datetime
from flask import Flask, request
from flask_restful import Resource, Api
from models import models

app = Flask(__name__)
api = Api(app)

class On(Resource):
    def get(self):
        models.criabancodedados(self)
        return {'status':'online'}

class Manga(Resource):
    def post(self):
        dados = request.json
        nome = dados['nome']
        capa = dados['capa']
        data = dados['data']
        status = dados['status']
        nota = dados['nota']
        sinopse = dados['sinopse']
        models.cadastromanga(capa, nome,data,status,nota,sinopse)
        return {'foi': 'sim'}

class Adm(Resource):
    def post(self):
        dados = request.json
        nome = dados['nome']
        email = dados['email']
        senha = dados['senha']
        models.cadastroadm(nome,email,senha)
        return {'foi':'sim'}

class User(Resource):
    def post(self):
        dados = request.json
        nome = dados['nome']
        email = dados['email']
        senha = dados['senha']
        data = dados['data']
        models.cadastrarusuarios(nome,email,senha,data)
        return {'foi':'sim'}

api.add_resource(On, '/')
api.add_resource(Adm, '/adm')
api.add_resource(User, '/user')
api.add_resource(Manga, '/manga')

if __name__ == '__main__':
    #port = int(os.environ.get("PORT", 5000))
    #app.run(host='0.0.0.0', port=port)
    app.run(debug=True)

