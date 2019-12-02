from flask_restful import Resource, reqparse, abort
from flask import jsonify, make_response
from src.database import get_db

class SampleAPI(Resource):
  def __init__(self):
    self.reqparse = reqparse.RequestParser()
    super(SampleAPI, self).__init__()

  def get(self):
    response_body = jsonify({"Hello":"World"})
    response = make_response(response_body, 200)
    response.headers['X-HogeHoge'] = 'hoge'
    return response