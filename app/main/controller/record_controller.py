from flask import request , make_response
from flask_restplus import Resource
from ..util.dto import RecordDto
from ..util.helpers import is_valid_epochtime
from ..service.record_service import get_all_records, get_record, create_record , delete_record, update_record
from app.main.util.decorator import admin_token_required,token_required



api = RecordDto.api
_record,_public_record = RecordDto.record, RecordDto.public_record
parser = api.parser()
parser.add_argument('Authorization', location='headers')

@api.route('/list')
class RecordList(Resource):

    @api.doc('list_of_records')
    @api.marshal_list_with(_public_record)
    def get(self):
        """List all records """
        return get_all_records()


@api.route('/read/<record_id>')
class Record(Resource):
    @api.doc('returns_record_instance')
    @api.marshal_list_with(_public_record)
    def get(self,record_id):
        """ returns record instance"""
        r =  get_record(record_id)
        if not r:
            api.abort(406,error=f"provided record_id {record_id} is not present in db or invalid.")
        return r



@api.expect(_record, validate=True)
@api.route('/create')
class RecordCreate(Resource):
    @api.doc('returns_record_instance')
    @api.marshal_with(_public_record)
    def post(self):
        """ returns record instance"""
        data = request.json
        ## verify if the timestamp is valid
        tstamp = data['timestamp']
        if is_valid_epochtime(tstamp): 
            return create_record(data) 
        else:
            api.abort(406,error=f"provided timestamp {tstamp} is not a valid epoch time.")



@api.expect(_record, validate=True)
@api.route('/modify/<record_id>')
class RecordUpdate(Resource):
    @api.doc('updates_record')
    @api.marshal_list_with(_public_record)
    def post(self,record_id):
        """ returns updated record"""
        data = request.json
        tstamp = data['timestamp']
        if get_record(record_id):
            if is_valid_epochtime(tstamp):
                return update_record(record_id,data)
            else:
                api.abort(406,error=f"updated epoch time for 'timestamp' is not valid or error in payload")
        else:
            api.abort(406,error=f"provided record_id {record_id} is not present in db.")



@api.route('/delete/<record_id>')
class RecordDelete(Resource):

    @api.expect(parser)
    @api.doc('deletes_record')
    @token_required
    @api.marshal_list_with(_public_record)
    def delete(self,record_id):
        """deletes record (auth token required. login user any to get auth token)"""
        if get_record(record_id):
            return delete_record(record_id)
        else:
            api.abort(406,error=f"provided record_id {record_id} is not present in db.")


