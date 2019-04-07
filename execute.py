import os
import unittest

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import blueprint
from app.main import create_app, db
from app.main.model import user, blacklist


app = create_app(os.getenv('CONFIG') or 'dev')
app.register_blueprint(blueprint)
app.app_context().push()

manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


@manager.command
def setupdb():
    db.create_all()
    db.session.commit()


@manager.command
def run():
    if os.getenv('CONFIG') == "dev":
        app.config.from_object('app.main.config.DevelopmentConfig')
    else:
        app.config.from_object('app.main.config.ProductionConfig')
    app.run()



@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == '__main__':
    manager.run()
