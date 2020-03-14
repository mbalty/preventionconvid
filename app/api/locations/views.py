from flask_restplus import Namespace, Resource, marshal
from flask_jwt_extended import jwt_required
from app.app_setup import flask_api
from app.api.locations.models import location_request, state_parser, location_response
from app.api.locations.service import LocationService
from app.api.common.models import auth_parser
from flask_jwt_extended import get_jwt_identity

locations_ns = Namespace('location', description="Location operations")

location_service = LocationService()


@locations_ns.expect(auth_parser)
@locations_ns.route('')
class Locations(Resource):
    """
    Create and Get Locations
    """
    @jwt_required
    @locations_ns.expect(location_request)
    def post(self):
        """
        Create A Location
        :return:
        """
        try:
            email = get_jwt_identity()
            payload = marshal(flask_api.payload, location_request)
            location_service.create_location(payload)
            return {'Message': "Location created successfully"}
        except Exception as ex:
            return {"Exception": ex}

    @locations_ns.expect(state_parser)
    @jwt_required
    def get(self):
        """
        Get Active, Archived and Deleted Locations
        :return:
        """
        email = get_jwt_identity()
        args = state_parser.parse_args()
        try:
            response = location_service.get_locations_user(args["user_id"])
        except Exception as ex:
            return {"Exception": str (ex)} 

        return {'Message': "Locations rendered successfully", 'records': marshal(response, location_response)}

    @staticmethod
    def validate_state(state):
        if state == 'active' or state == 'archived' or state == 'deleted':
            return True
        else:
            return False

