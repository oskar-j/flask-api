#!/usr/bin/python
# -*- coding: utf-8 -*-

from api.utils.database import db
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields
from api.models.model_location_group import LocationGroupSchema
from api.models import Base


class Country(Base):

    __tablename__ = 'country'

    # Longest country code is a 6-length char "ITU callsign prefixes"
    # Shortest are made of 2 chars
    # https://en.wikipedia.org/wiki/Country_code
    country_code = db.Column(db.String(80), unique=True, nullable=False)

    # Country is linked with LocationGroup via one to many relationship
    location_groups = db.relationship('LocationGroup', backref='country', lazy=True)

    def __init__(self, country_code, location_groups=[]):
        self.country_code = country_code
        self.location_groups = location_groups

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __repr__(self):
        return '<Country: %r>' % self.country_code


class CountrySchema(ModelSchema):

    class Meta(ModelSchema.Meta):
        model = Country
        sqla_session = db.session

    id = fields.Number(dump_only=True)
    country_code = fields.String(required=True)

    date_created = fields.String(dump_only=True)
    date_updated = fields.String(dump_only=True)

    location_groups = fields.Nested(LocationGroupSchema, many=True)
