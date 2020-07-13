from flask import Flask
from flask_restx import Api,Resource

app = Flask(__name__)
api = Api(app,version="1.0",title="Demo_flask_restx")

@api.route('/demo')
class MyResource(Resource):
    @api.response(200,"Success")
    @api.response(500,"Internal Server Error")
    def get(self):
        try:
            return {"Status":200,"message":"Success"}
        except:
            return {"Status":500,"message":"Internal Server error"}
            
app.run(debug=True)