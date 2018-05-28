#!/usr/bin/python
# -*- coding: utf-8 -*-
from api.models.model_location_group import LocationGroup
from api.utils.database import db
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields
from api.models import Base


# Location is linked with LocationGroup via many to many relationship:
location_groups = db.Table('location_groups',
                           db.Column('location_id', db.Integer, db.ForeignKey('location.id'), primary_key=True),
                           db.Column('location_group_id', db.Integer, db.ForeignKey('location_group.id'), primary_key=True)
                           )


class Location(Base):

    __tablename__ = 'location'

    name = db.Column(db.String(12), unique=True, nullable=False)
    external_id = db.Column(db.String(12), unique=True, nullable=False)
    secret_code = db.Column(db.String(12), unique=True, nullable=False)

    location_groups = db.relationship('LocationGroup', secondary=location_groups,
                                      lazy='subquery', backref=db.backref('locations', lazy=True))

    def __init__(self, name, external_id, secret_code):
        self.name = name
        self.external_id = external_id
        self.secret_code = secret_code

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __repr__(self):
        return '<Location: %r>' % self.name


class LocationSchema(ModelSchema):

    class Meta(ModelSchema.Meta):
        model = Location
        sqla_session = db.session

    id = fields.Number(dump_only=True)
    name = fields.String(required=True)

    date_created = fields.String(dump_only=True)
    date_updated = fields.String(dump_only=True)

    external_id = fields.String(required=True)
    secret_code = fields.String(required=True)

    location_groups = fields.Nested(LocationGroup, many=True)
