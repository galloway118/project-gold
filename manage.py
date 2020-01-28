from BookModel import app, db
from BookModel import Book, User
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

manager = Manager(app)
migrate = Migrate(app, db)


manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
