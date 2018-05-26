#!/usr/bin/python
# -*- coding: utf-8 -*-

from api.utils.database import db
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields
from api.models import Base


class TargetGroup(Base):

    __tablename__ = 'target_group'

    name = db.Column(db.String(24), unique=True, nullable=False)
    external_id = db.Column(db.String(12), unique=True, nullable=False)

    # TargetGroup model would have associations with it self
    # via parent_id which would form a tree with multiple root nodes
    parent_id = db.Column(db.Integer, db.ForeignKey('target_group.id'), nullable=True)

    secret_code = db.Column(db.String(12), unique=True, nullable=False)
    panel_provider_id = db.Column(db.Integer, db.ForeignKey('panel_provider.id'), nullable=False)

    def __init__(self, name, external_id, secret_code, panel_provider_id, parent_id=None):
        self.name = name
        self.external_id = external_id
        self.parent_id = parent_id
        self.secret_code = secret_code
        self.panel_provider_id = panel_provider_id

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __repr__(self):
        return '<TargetGroup: %r>' % self.name


class TargetGroupSchema(ModelSchema):

    class Meta(ModelSchema.Meta):
        model = TargetGroup
        sqla_session = db.session

    id = fields.Number(dump_only=True)
    name = fields.String(required=True)

    date_created = fields.String(dump_only=True)
    date_updated = fields.String(dump_only=True)
