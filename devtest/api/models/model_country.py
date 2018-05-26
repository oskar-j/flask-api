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
    country_code = db.Column(db.String(6), unique=True, nullable=False)

    panel_provider_id = db.Column(db.Integer, db.ForeignKey('panel_provider.id'), nullable=False)

    # Country is linked with LocationGroup via one to many relationship
    location_groups = db.relationship('LocationGroup', backref='country', lazy=True)

    def __init__(self, country_code, panel_provider_id, location_groups=[]):
        self.country_code = country_code
        self.panel_provider_id = panel_provider_id
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
    panel_provider_id = fields.Integer(required=True)

    date_created = fields.String(dump_only=True)
    date_updated = fields.String(dump_only=True)

    location_groups = fields.Nested(LocationGroupSchema, many=True, required=False)
