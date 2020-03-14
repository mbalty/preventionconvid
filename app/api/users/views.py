from flask import request
from flask_restplus import Namespace, Resource, marshal
from app.app_setup import flask_api
from app.api.users.models import user_request, user, user_base
from app.api.users.service import UserService

users_ns = Namespace('users', description='User Management')
user_service = UserService()


@users_ns.route('')
class Users(Resource):
    '''
    Add Users
    '''
    @users_ns.expect(user_request)
    def post(self):
        """

        :return:
        """
        payload = marshal(flask_api.payload, user_request)
        user_service.signup(payload)
        return {'status': 'Signed up Successfully', 'status_code': 200}


@users_ns.route('/activate/<string:id>')
class UserActivate(Resource):
    """
    Activate User
    """

    def get(self, id):
        """
        Activate the User
        :param id:
        :return:
        """
        user_service.activate(id)
        return {'status': "User Activated Successfully", 'status_code': 200}