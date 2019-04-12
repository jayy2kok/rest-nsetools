from flask import Flask
from flask_jsonpify import jsonify
from flask_restful import Resource, Api
from nsetools import Nse


app = Flask(__name__)
api = Api(app)
nse = Nse()

class StockQuotes(Resource):
    def get(self, code):
        q = nse.get_quote(code)
        return jsonify(q)

class IndexQuotes(Resource):
    def get(self,indexCode):
        q=nse.get_index_quote(indexCode)
        return jsonify(q)

class Indexes(Resource):
    def get(self):
        q=nse.get_index_list()
        return jsonify(q)

class Stocks(Resource):
    def get(self):
        q = nse.get_stock_codes(cached=False)
        return jsonify(q)

api.add_resource(StockQuotes, '/stock-quotes/<code>')
api.add_resource(IndexQuotes, '/index-quotes/<indexCode>')
api.add_resource(Indexes, '/indexes')
api.add_resource(Stocks, '/stocks')



if __name__== '__main__':
    app.run(host='127.0.0.1', port=9090, debug=True)
