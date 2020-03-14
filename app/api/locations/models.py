from flask_restplus import fields, reqparse
from app.app_setup import flask_api
from app.api.common.models import meta
from app.utils.date_utils import get_current_time

state_parser = reqparse.RequestParser()
state_parser.add_argument('State', type=str, location='args')

location_request = flask_api.model('location_request', {
    'user_id': fields.String(required=True, description="user_id"),
    'latitude': fields.Float(required=True, description="latitude"),
    'longitude': fields.Float(required=True, description="longitude"),
    'start_time': fields.String(required=True, description="start_time"),
    'end_time': fields.String(required=True, description="end_time")
})

location_record = flask_api.inherit('location_record', location_request, {
    '_id': fields.Nested(fields.String())
})

location_response = flask_api.inherit('location_response', location_request, {
    '_id': fields.Nested(fields.String())
})

