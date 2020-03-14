from app.app_setup import application, flask_api
from app.api.users.views import users_ns
from app.api.auth.views import auth_ns
from app.api.locations.views import locations_ns


flask_api.add_namespace(users_ns, '/api/v1/users')
flask_api.add_namespace(auth_ns, '/api/v1/auth')
flask_api.add_namespace(locations_ns, '/api/v1/locations')

if __name__ == '__main__':
    application.run(host='0.0.0.0')

