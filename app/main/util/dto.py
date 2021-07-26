from flask_restplus import Namespace

class ExchangeDto:
    api = Namespace('exchange', description='exchange related operations')