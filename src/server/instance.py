from flask import Flask
from flask_restplus import Api


class Server:
    def __init__(self, ):
        self.app = Flask(__name__)
        self.api = Api(self.app,
                       version="2.0",
                       title="Easydoc OCR",
                       description="API especializada na extração do conteúdo textual de documentos.",
                       # doc='/doc/',
                       default="Endpoints",
                       default_label="Rotas de acesso",
                       catch_all_404s=True,
                       )

    def run(self):
        self.app.run(debug=True)


server = Server()
