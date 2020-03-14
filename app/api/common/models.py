from flask_restplus import fields, reqparse
from app.app_setup import flask_api
from app.utils.date_utils import get_current_time
import werkzeug

meta = flask_api.model('meta', {
    'created_on': fields.DateTime(default=get_current_time()),
    'updated_on': fields.DateTime(default=get_current_time())
})

auth_parser = reqparse.RequestParser()
auth_parser.add_argument('Authorization', location='headers')
