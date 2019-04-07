from app.main import db
from app.main.model.record import Record 
import time

def get_all_records():
    return Record.query.all()


def update_record(record_id,data):
    record = Record.query.filter_by(_id=record_id).first()
    record.lastModificationDate = time.time()
    if data:
        if data['timestamp'] != record.timestamp:
            record.timestamp = data['timestamp']
        if data['value1'] != record.value1:
            record.value1 = data['value1']
        if data['value2'] != record.value2:
            record.value2 = data['value2']
        if data['value3'] != record.value3:
            record.value3 = data['value3']
            
    db.session.commit()
    db.session.refresh(record)
    _id = record._id
    return get_record(_id)


def delete_record(data):
    print(data)
    record = Record.query.filter_by(_id=data).first()
    db.session.delete(record)
    db.session.commit()
    return record


def create_record(data):
    new_record = Record(
        timestamp=data['timestamp'],
        value1=data['value1'],
        value2=data['value2'],
        value3=data['value3'],
        creationDate=float(time.time()),
        lastModificationDate=float(time.time())
    )
    save_changes(new_record)
    db.session.refresh(new_record)
    _id = new_record._id 
    return get_record(_id)
    


def get_record(record_id):
    return Record.query.filter_by(_id=record_id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()

