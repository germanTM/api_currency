from flask_restplus import Api
from flask import Blueprint

from .main.controller.exchange_controller import api as ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='FLASK EXCHANGE TRANSACTIONS API',
          version='1.0',
          description='An api to visualize info and make transactions between currencies'
          )

api.add_namespace(ns, path="/exchange")
