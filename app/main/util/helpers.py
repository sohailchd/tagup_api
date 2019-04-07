
import datetime , time


def is_valid_epochtime(tstamp):
    '''
        verifies if the given time is valid
        it is assumed that consumer may even send 0 as timestamp 
        * requirement not clear *
    '''
    try:
        param_date = datetime.datetime.fromtimestamp(tstamp)
        return isinstance(param_date,datetime.datetime)
    except Exception as e:
        print(e)
        return False