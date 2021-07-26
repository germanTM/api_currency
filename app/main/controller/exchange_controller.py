from flask import request, abort
from ..util.dto import ExchangeDto
from flask_restplus import Resource, api
from app.error_handler import InvalidExchangeData
from ..service.exchange_service import exchange_info, make_transaction

api = ExchangeDto.api

@api.route("/")
class ExchangeRate(Resource):
    @api.doc('Get exchange rate and fee amount')
    def post(self):
        """Get exchange rate and fee amount between two currencies"""
        try:
            data = request.get_json()
            return exchange_info(data=data)
        except InvalidExchangeData as e:
            abort(e.status_code, e.message)
        

@api.route("/transaction")
class ExchangeTransaction(Resource):
    @api.response(201, 'Transaction made successfully')
    @api.doc('Make transaction between currencies')
    @api.expect(validate=True)
    def post(self):
        """Make exchange transaction between the two selected currencies"""
        try:
            data = request.get_json()
            return make_transaction(data=data)
        except InvalidExchangeData as e:
            abort(e.status_code, e.message) 
        
