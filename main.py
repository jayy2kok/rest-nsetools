from flask import Flask
from nsetools import Nse
from flask.ext.jsonpify import jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
nse = Nse()

class StockQuotes(Resource):
    def get(self, code):
        q = nse.get_quote(code)
        return jsonify(q)

api.add_resource(StockQuotes, '/stock-quotes/<code>')

if __name__== '__main__':
    app.run(host='127.0.0.1', port=9090, debug=True)
