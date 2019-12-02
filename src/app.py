from flask import Flask, jsonify, request
from flask_restful import Api
from flask_cors import CORS

from src.apis.sample import SampleAPI

def create_app():
  app = Flask(__name__)
  app.config['JSON_AS_ASCII'] = False
  cors = CORS(app, resources={r"*": {"origins":"*"}})
  api = Api(app)

  api.add_resource(SampleAPI, '/sample')
  

  return app

app = create_app()