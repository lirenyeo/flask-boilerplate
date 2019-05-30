from flask import Blueprint, make_response, jsonify

users_api_blueprint = Blueprint('users_api',
                             __name__,
                             template_folder='templates')

@users_api_blueprint.route('/', methods=['GET'])
def index():
    response = {
        "status": "success"
    }
    return make_response(jsonify(response)), 200
