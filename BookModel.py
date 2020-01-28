from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import json
from settings import app
from flask_seeder import FlaskSeeder

db = SQLAlchemy(app)
seeder = FlaskSeeder()
db.init_app(app)
seeder.init_app(app, db)


class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float, nullable=False)
    isbn = db.Column(db.Integer)

    def __init__(self, name, price, isbn):
        self.name = name
        self.price = price
        self.isbn = isbn

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'isbn': self.isbn
        }


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer)

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price

        }
