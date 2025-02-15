from flask import Blueprint
from flask_restx import Api, Namespace


blueprint_tiktok = Blueprint('api', __name__, url_prefix='/api')


app_ns = Namespace('app', ordered=True, validate=True, path='/',
                    description='titkok users management',
                    security=None)

# authorizations = {
#     'apikey': {
#         'type': 'apiKey',
#         'in': 'header',
#         'name': 'Authorization'
#     }
# }

api = Api(blueprint_tiktok)
api.add_namespace(app_ns)