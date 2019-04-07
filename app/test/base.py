
from flask_testing import TestCase

from app.main import db
from execute import app
import logging
 
logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger('TestRecord')

class BaseTestCase(TestCase):

    def create_app(self):
        app.config.from_object('app.main.config.TestingConfig')
        return app

    @classmethod
    def setUpClass(cls):
        db.create_all()
        db.session.commit()
        log.debug("DB created.")

    @classmethod
    def tearDownClass(cls):
        db.session.remove()
        db.drop_all()
        log.debug("DB destroyed.")