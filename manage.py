from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from api import app
from api.models.model_mixin import db


manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
