from flask import Flask, request, make_response, Blueprint
from Utilities.utility import *

some_api_bp=Blueprint("Flask API",__name__)

@some_api_bp.route('/', methods=['GET'])
def some_get_api():
    func()
    return make_response({"output": "Hello"}, 200)

@some_api_bp.route('/<input>', methods=['GET'])
def input_get_api(input):
    
    return make_response({"output": "This was the input "+input}, 200)


@some_api_bp.route('/', methods=['POST'])
def some_post_api():
    body = request.get_json()   
    if not body:
        return make_response({'error': 'Provide relevent body details'}, 400)
    else:
        if 'input' not in body:   
            return make_response({'error': 'Provide relevent body details'}, 400)
    
    input = body['input']
        
    return make_response({"output": "This was the input "+input}, 200)