from flask_restplus import abort
from flask_restplus.inputs import email
from bson import ObjectId
from passlib.hash import sha256_crypt
from app.api.users.models import user
from app.utils.db_utils import Base
from app.utils.mail_utils import send_mail
from app.utils.helper import custom_marshal
from app.api.common.constants import Collections, ACTIVATION_MAIL

base_obj = Base()


class UserService(object):
    """
    Service Class for User View
    """

    def signup(self, payload):
        """
        signup function
        :return:
        """

        try:
            check_email = email(check=True)
            payload["email"] = check_email(payload["email"])
        except Exception as ex:
            abort(400, Message="Invalid email")
        if payload.get('password') != payload.get('confirm_password'):
            abort(400, Message="Password does not match")
        count, records = base_obj.get(Collections.USERS, {"email": payload['email']})
        if count > 0:
            abort(400, Message="Email ID Already Exists")
        payload = custom_marshal(payload, user, 'create')
        payload['password'] = sha256_crypt.encrypt(payload['password'])
        _id = base_obj.insert(Collections.USERS, payload)
        print(_id, type(_id))
        link = ACTIVATION_MAIL.format(id=_id)
        print(link)
        send_mail([payload['email']],"Corona Location App Account Activation", link, 'signup.html', {'link': link, 'name': payload['first_name']})

    def activate(self, id):
        """
        Activate the user
        :param id:
        :return:
        """
        count, records = base_obj.get(Collections.USERS, {"_id": ObjectId(id)})
        if count == 0:
            abort(400, Message="Invalid Link")
        if records[0]['is_active']:
            abort(400, Message="Account Already Active")
        else:
            base_obj.update(Collections.USERS, {"_id": ObjectId(id)}, {"$set": {"is_active": True}})
