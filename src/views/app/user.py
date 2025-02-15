from flask_restx import fields

from src.views.blueprint import api, app_ns
from src.views.resources import ResourceApp
from src.views import json_response
from src.lib.app.user import create_user
from src.lib.app.user import get_user



tiktok_post_model = app_ns.model('tiktok_post_model', {
    'username': fields.String(required=True, description='name of the book'),
})


@app_ns.route('/tiktok_users/add', doc={'example': 'tiktok_users/add'})
class AddTiktokUser(ResourceApp):
    @app_ns.expect(tiktok_post_model)
    def post(self):
        status_code, data = create_user(api.payload)
        if status_code == 201:
            return json_response(status_code=status_code, data=data)
        elif status_code == 404:
            return json_response(status_code=status_code, trace=data)
        else:
            return json_response(status_code=500, trace="internal server error")
        
        
        
        
        
@app_ns.route('/tiktok_users/<user_ref>', doc={'example': 'tiktok_users/134'})
class GetUser(ResourceApp):
    def get(self, user_ref):

        status_code, data = get_user(user_ref)
        if status_code == 200:
            return json_response(status_code=status_code, data=data)
        elif status_code == 404:
            return json_response(status_code=400, trace=data['trace'])
        else:
            return json_response(status_code=500, trace="internal server error")
