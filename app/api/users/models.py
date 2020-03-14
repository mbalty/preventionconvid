from flask_restplus import fields
from app.app_setup import flask_api
from app.api.common.models import meta
from app.utils.date_utils import get_current_time

user_base = flask_api.model('signup',{
    'email': fields.String(description="Email ID"),
    'phone_number': fields.String(despcription="Phone Number"),
    'first_name': fields.String(description="First Name"),
    'last_name': fields.String(description="Last Name"),
    'password': fields.String(description="Password"),
    "user_type": fields.String(description="doctor / patient")
})

user_request = flask_api.inherit('user base', user_base, {
    'confirm_password': fields.String(description="Confirm password")
})

user = flask_api.inherit('user', user_base, {
    'is_active': fields.Boolean(default=False, description="Account Activated or Not"),
    'is_sick': fields.Boolean(default=False, description="User signaled as sick"),
    'meta': fields.Nested(meta)
})
