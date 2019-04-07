from flask import request , render_template, make_response
from flask_restplus import Resource, Namespace, fields



api = Namespace("")


@api.route('/',doc=False)
@api.hide
class HomePage(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template("index.html",name="test"),200,headers)
