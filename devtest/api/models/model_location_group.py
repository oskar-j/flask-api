#!/usr/bin/python
# -*- coding: utf-8 -*-

from api.utils.database import db
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields
from api.models import Base
from api.models.model_panel_provider import PanelProvider


class LocationGroup(Base):

    __tablename__ = 'location_group'

    name = db.Column(db.String(12), unique=True, nullable=False)

    # Country is linked with LocationGroup via one to many relationship
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'), nullable=False)

    panel_provider_id = db.Column(db.Integer, db.ForeignKey('panel_provider.id'), nullable=False)

    def __init__(self, name, country_id, panel_provider_id):
        self.name = name
        self.country_id = country_id
        self.panel_provider_id = panel_provider_id

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __repr__(self):
        return '<LocationGroup: %r>' % self.name


class LocationGroupSchema(ModelSchema):

    class Meta(ModelSchema.Meta):
        model = LocationGroup
        sqla_session = db.session

    id = fields.Number(dump_only=True)
    name = fields.String(required=True)

    date_created = fields.String(dump_only=True)
    date_updated = fields.String(dump_only=True)

    country_id = fields.Integer()
    panel_provider_id = fields.Integer()
