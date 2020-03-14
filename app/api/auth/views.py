from flask_restplus import Namespace, Resource
from flask_jwt_extended import jwt_required
from app.app_setup import flask_api, redis_store
from app.api.auth.models import login
from app.api.auth.service import AuthService
from app.api.common.models import auth_parser
from flask_jwt_extended import get_raw_jwt

auth_ns = Namespace('auth', description="User Authentication")

auth_service = AuthService()

@auth_ns.route('/login')
class AuthLogin(Resource):
    """
    Authentication APIs for Login
    """
    @auth_ns.expect(login)
    def post(self):
        """
        Login Request
        :return:
        """
        response = auth_service.login(flask_api.payload)
        return response

@auth_ns.expect(auth_parser)
@auth_ns.route('/logout')
class AuthLogout(Resource):
    """
    Authentication API for logout
    """

    @jwt_required
    def post(self):
        """
        Logout Request
        :return:
        """
        jti = get_raw_jwt()['jti']
        ttl = redis_store.ttl(jti)
        redis_store.set(jti, 'true', ttl)
        return {'status': "Logged out successfully"}