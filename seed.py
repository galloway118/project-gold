from BookModel import Book, User
from BookModel import db


Tom = Book(name="chris", price="2.99", isbn='292020302')
Rish = Book(name="Rish", price="2.99", isbn='292020302')
Jack = Book(name="Jack", price="2.99", isbn='292020302')
Rhianon = Book(name="Rhianon", price="2.99", isbn='292020302')
Amelia = Book(name="Amelia", price="2.99", isbn='292020302')
Lewis = Book(name="Lewis", price="2.99", isbn='292020302')


db.drop_all()
db.create_all()

db.session.add(Tom)
db.session.add(Rish)
db.session.add(Jack)
db.session.add(Rhianon)
db.session.add(Amelia)
db.session.add(Lewis)
db.session.commit()

# SQLAlchemy database model


# class User(Base):
#     def __init__(self, id_num=None, name=None, age=None):
#         self.id_num = id_num
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return "ID=%d, Name=%s, Age=%d" % (self.id_num, self.name, self.age)

# All seeders inherit from Seeder


# class DemoSeeder(Seeder):

#     # run() will be called by Flask-Seeder
#     def run(self):
#         # Create a new Faker and tell it how to create User objects
#         faker = Faker(
#             cls=user,
#             init={
#                 "id": generator.Sequence(),
#                 "name": generator.Name(),
#                 "age": generator.Integer(start=20, end=100)
#             }
#         )

#         # Create 5 users
#         for user in faker.create(5):
#             print("Adding user: %s" % user)
#             self.db.session.add(user)
