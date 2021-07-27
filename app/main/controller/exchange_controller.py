from flask import request, abort
from ..util.dto import ExchangeDto
from flask_restplus import Resource, api, fields
from app.error_handler import InvalidExchangeData
from ..service.exchange_service import exchange_info, make_transaction

api = ExchangeDto.api

@api.route("/getFeeAndRate")
class ExchangeRate(Resource):
    fee_and_rate_request_fields = api.model('fee_and_rate_request', {
        'from_currency': fields.Float,
        'to_currency': fields.Float,
        'evaluate_amount': fields.Float
    })

    fee_and_rate_response_fields = api.model('fee_and_rate_response', {
        'exchange_rate': fields.Float,
        'fee_amount': fields.Float,
    })

    #Normally this should be a GET method but because of the challenge restraints for all the enpoints to receive and return JSON data it was implemented as a POST method
    @api.doc('Get exchange rate and fee amount')
    @api.expect(fee_and_rate_request_fields)
    @api.response(201, 'Success processing the request', fee_and_rate_response_fields)
    def post(self):
        """Get exchange rate and fee amount between two currencies"""
        try:
            data = request.get_json()
            return exchange_info(data=data)
        except InvalidExchangeData as e:
            abort(e.status_code, e.message)
        

@api.route("/transaction")
class ExchangeTransaction(Resource):

    transaction_response_fields = api.model('transaction_response', {
        'from_currency': fields.Float,
        'to_currency': fields.Float,
        'exchange_amount': fields.Float
    })

    transaction_request_fields = api.model('transaction_request', {
        'exchange_rate': fields.Float,
        'fee_amount': fields.Float,
        'accumulated_fee_over_base': fields.Float
    })

    @api.response(201, 'Success processing the request', transaction_response_fields)
    @api.doc('Make transaction between currencies')
    @api.expect(transaction_request_fields)
    def post(self):
        """Make exchange transaction between the two selected currencies"""
        try:
            data = request.get_json()
            return make_transaction(data=data)
        except InvalidExchangeData as e:
            abort(e.status_code, e.message) 
        
