#!/usr/bin/python
# -*- coding: utf-8 -*-

from api.utils.database import db
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields
from api.models import Base


class PanelProvider(Base):

    __tablename__ = 'panel_provider'

    code = db.Column(db.String(12), unique=True, nullable=False)

    # TODO: do we need this?
    # location_groups = db.relationship('LocationGroup', backref='panel_provider', lazy=True)

    def __init__(self, code, location_groups=[]):
        self.code = code
        self.location_groups = location_groups

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __repr__(self):
        return '<PanelProvider: %r>' % self.code


class PanelProviderSchema(ModelSchema):

    class Meta(ModelSchema.Meta):
        model = PanelProvider
        sqla_session = db.session

    id = fields.Number(dump_only=True)
    code = fields.String(required=True)

    date_created = fields.String(dump_only=True)
    date_updated = fields.String(dump_only=True)
