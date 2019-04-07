from .. import db
import time
from sqlalchemy import func
from sqlalchemy import types




class Record(db.Model):
    '''
        schema for record:
        {
            "_id": id,
            "timestamp": timestamp,                        ## creation of record on client end
            "value1": value1,                              ## int
            "value2": value2,                              ## float
            "value3": value3,                              ## boolean
            "creationDate": creationDate,                  ## database insertion time
            "lastModificationDate": lastModificationDate   ## modification timestamp 
        }
    '''
    __tablename__ = "records"
    _id = db.Column(db.Integer,primary_key=True, autoincrement=True)
    timestamp = db.Column(db.Float, nullable=False)
    value1 = db.Column(db.Integer, nullable=False)
    value2 = db.Column(db.Integer, nullable=False)
    value3 = db.Column(db.Boolean,nullable=False)
    creationDate = db.Column(db.Float,nullable=False)
    lastModificationDate = db.Column(db.Float,nullable=False)


    def update(self,data={}):
        '''
        '''
        if  data['timestamp'] : self.timestamp = data['timestamp']
        if  data['value1'] : self.value1 = data['value1']
        if  data['value2'] : self.value2 = data['value2']
        if  data['value3'] : self.value3 = data['value3']
    

    def __repr__(self):
        return f"<Record '{self.timestamp,self.value1,self.value2,self.value3}'>"