from flask import Flask, request, make_response, Blueprint
from flask_restx import  Resource, Api, reqparse, Namespace
from Utilities.utility import *

#APi using falsk_restx

another_api_bp=Blueprint("",__name__)
api = Api(another_api_bp, version='1.0', title='Another API', description='Sample API')

restx_api_ns = api.namespace(name='Flask restx API sample', description='Namespace for Flask restx API sample')

parser = reqparse.RequestParser()
parser.add_argument('input', type=str, required=True, help= 'Some Input')

@restx_api_ns.route('/')
class AddUser(Resource):
    @restx_api_ns.expect(parser)
    def post(self):
        args = parser.parse_args() 
        input = args['input']

        return make_response({"output": "This was the input "+input}, 200)
