from flask_restplus import Resource

from src.server.instance import server
from src.models.books import book

app, api = server.app, server.api

books_db = [
    {"id": 0, 'title': "Clean code"},
    {"id": 1, 'title': "Lixo book"}
]


@api.route('/books')
class BookList(Resource):
    @api.marshal_list_with(book, mask=False)
    def get(self):
        return books_db

    @api.expect(book, validate=True)
    @api.marshal_with(book, mask=False)
    def post(self):
        response = api.payload
        print(response)
        books_db.append(response)
        return response, 200
