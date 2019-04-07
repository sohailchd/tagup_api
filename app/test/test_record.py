import unittest
from app.main.model.record import Record
from app.test.base import BaseTestCase,log
import json


class TestRecord(BaseTestCase):

    def test_0_create_new_record(self):
        response =  self.client.post(
                '/api/create',
                data=json.dumps(dict(
                    timestamp=121212,
                    value1=1,
                    value2=2,
                    value3=True,
                )),
                content_type='application/json'
        )
        rdata = json.loads(response.data.decode())
        log.debug(rdata)



#  response = register_user(self)
#             data = json.loads(response.data.decode())
#             self.assertTrue(data['status'] == 'fail')
#             self.assertTrue(
#                 data['message'] == 'User already exists. Please Log in.')
#             self.assertTrue(response.content_type == 'application/json')
#             self.assertEqual(response.status_code, 409)


    def test_1_read_record(self):
        response =   self.client.get(
            '/api/read/1',
            content_type='application/json'
        )
        rdata = json.loads(response.data.decode())
        self.assertTrue(response.content_type == 'application/json')
        self.assertEqual(response.status_code,200)
        log.debug(rdata)
        assert rdata['timestamp'] == 121212.0 
        assert rdata['value1'] == 1 
        assert rdata['value2'] == 2.0 
        assert rdata['value1'] == True  

    
    def test_2_modify_record(self):
        response =   self.client.post(
            '/api/modify/1',
            data=json.dumps(dict(
                    timestamp=56565678,
                    value1=1,
                    value2=2,
                    value3=True,
                )),
            content_type='application/json'
        )
        rdata = json.loads(response.data.decode())
        log.debug(rdata)
        self.assertTrue(response.content_type == 'application/json')
        self.assertEqual(response.status_code,200)
        assert rdata['timestamp'] == 56565678.0 

    def test_3_delete_record_without_auth(self):
        response =   self.client.post(
            '/api/delete/1',
            content_type='application/json',
        )
        rdata = json.loads(response.data.decode())
        self.assertTrue(response.content_type == 'application/json')
        ## deleting without auth token
        self.assertEqual(response.status_code,405)
       
