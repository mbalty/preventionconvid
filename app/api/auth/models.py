from app.app_setup import flask_api
from flask_restplus import fields

login = flask_api.model('login',{
    'email': fields.String(required=True, description="Enter Email ID"),
    'password': fields.String(required=True, description="Enter Password")
})
