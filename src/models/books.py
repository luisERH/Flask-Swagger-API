from flask_restplus import fields
from src.server.instance import server

book = server.api.model('Book', {
    'id': fields.Integer(description='O id di registro.'),
    'title': fields.String(required=True, min_length=1, max_length=200, description='{id : "X" , "title" : "XXX"}')
})
