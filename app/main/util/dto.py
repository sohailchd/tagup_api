from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'public_id': fields.String(description='user Identifier')
    })


class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })


class RecordDto:
    api = Namespace('record', description='iot event records')
    record = api.model('record', {
        'timestamp': fields.Float(required=True, description='Unix_epoch timestamp of the event.'),
        'value1': fields.Integer(required=True, description='integer value1.'),
        'value2': fields.Float(required=True, description='float value2.'),
        'value3': fields.Boolean(required=True, description='integer value3.'),
    })

    public_record = record.inherit('record', {
    '_id': fields.Integer
    })