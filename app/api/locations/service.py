from bson import ObjectId
from flask_restplus import abort
from flask_jwt_extended import get_jwt_identity
from app.api.locations.models import location_request, location_record
from app.utils.db_utils import Base
from app.utils.helper import custom_marshal, update_timestamp
from app.api.common.constants import Collections

base_obj = Base()


class LocationService(object):
    """
    Service Class for Location
    """
    def create_location(self, payload):
        """
        Create Location for an User
        :param payload:
        :return:
        """
        payload = custom_marshal(payload, location_record, 'create')
        _id = base_obj.insert(Collections.LOCATIONS, payload)

    def get_locations_user(self, user_id):
        """
        Get Locations for a particular User
        :param email:
        :return:
        """
        query = {"user_id": ObjectId(user_id)}

        count, records = base_obj.get(Collections.LOCATIONS, query)

        return records
    
    def get_locations_user_date_range(self, user_id, start_date, end_date):
        """
        Get Locations for a particular User, in date range
        :param email:
        :param start_date:
        :param end_date:
        :return:
        """
        pass #TODO: implement

    def delete_location(self, location_id):
        """
        Delete Location
        :param location_id:
        :return:
        """
        result = base_obj.delete(Collections.LOCATIONS, {"_id": ObjectId(id)})
        if not result.modified_count:
            abort(401, Message="Unauthorized")
            
    def delete_locations_by_user(self, location_id, user_id):
        """
        Delete Location
        :param location_id:
        :param user_id:
        :return:
        """
        result = base_obj.delete(Collections.LOCATIONS, {"_id": ObjectId(id), "user_id": ObjectId(user_id)})
        if not result.modified_count:
            abort(401, Message="Unauthorized")

    

    