from flask import Flask
from flask_restful import Api
from resorces.book import Books # eu sei que "resorce" está escrito errado


app = Flask(__name__)
api = Api(app)

api.add_resource(Books, '/<string:author_name>')

@app.after_request
def add_header(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "*")
    response.headers.add("Access-Control-Allow-Methods", "*")

    return response


if __name__ == '__main__': 
    app.run(debug=True)
