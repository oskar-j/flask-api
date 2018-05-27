from flask_script import Manager  # class for handling a set of commands
from flask_migrate import Migrate, MigrateCommand
from api.utils.factory import create_app
from api.utils.database import db
from api.utils.config import DevelopmentConfig


app = create_app(DevelopmentConfig)


migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
