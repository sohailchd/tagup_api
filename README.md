#### Tagup backend project


### Assumptions made 
    1. API consumer is saving some sort of records in following format, which will come as json paylod in body     
    {   
        "timestamp": timestamp,
        "value1": value1,   
        "value2": value2,   
        "value3": value3   
    }   

    2. 'timestamp' provided by the consumer payload can be zero (in future or in past too). If not the case, we just  have   
        to change the 'is_valid_epochtime' validation in app/main/util/helpers.py. 


### Terminal commands for local testing in sqlite3

    $ export CONFIG=dev
    $ make setup_testdb   ## creates tables without overwritting existing one.   
    $ make run            ## stars the server 

    **Make sure export CONFIG=dev  is properly set for local testing

    Running all the test cases 
    -------------------------
    $ export CONFIG=test   
    $ make tests   

### Viewing the app ###

    Open the following url on your browser to view home page 
    http://127.0.0.1:5000/


    Documentation:
    http://127.0.0.1:5000/doc



#### Understanding DIR structure  
```   
   ──  app                                 ## our main app    
    │   ├── main
    │   │   ├── config.py
    │   │   ├── controller                 ## all the enpoints  
    │   │   ├── model                      ## db schema   
    │   │   ├── service                    ## all the db session related stuffs    
    │   │   ├── templates                  ## any static templates     
    │   │   └── util                       ## helper functions and Dto objects      
    │   └── test                           ## test cases       
    ├── execute.py                         ## runner script      
    ├── Makefile                           
    ├── migrations   
    ├── Procfile                           ## Heroku build file   
    ├── README.md   
    └── requirements.txt    
```

#### Heroku 
    link : https://pacific-garden-71382.herokuapp.com
    On heroku postgres db is integrated. 

### Notes:
    Authentication module has been added. Currently only /delete/:record_id is secured for testing.  
    To secure any endpint we need to add decorator @token_required and it should ask for auth token, which    
    can be obtained by creating any user or loging in any exiting user. Copy from the response.   

    Purposely I am avoiding one-to-one relation between user and records table to keep it simple, for now.
    Just a matter of adding a foreign and few filters in db calls.  
 
###
    Built with -
    Python, Flask, Swagger, Flask_restplus 

    Easy to change pucblic facing data by changing Dto in single file. (app/main/util/dto.py)
    Easy to authenticate.
    Easy to maintain in long run.
    All the code is modularised, avoids dependceny on each other and eash to extend. 

