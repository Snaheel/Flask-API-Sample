from flask import Flask
from flask_restx import Api
from flask_cors import CORS
from API.some_api import some_api_bp
from API.another_api import another_api_bp

app = Flask(__name__)
app.register_blueprint(some_api_bp, url_prefix="/api/v1/some_endpoint")
app.register_blueprint(another_api_bp, url_prefix="/api/v1/some_other_endpoint")

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)