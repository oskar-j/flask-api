#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import request

from api.models.model_panel_provider import PanelProvider, PanelProviderSchema
from api.utils.responses import response_with
from api.utils import responses as resp
from api.models.model_country import Country, CountrySchema
from api.models.model_location import Location, LocationSchema
from api.models.model_target_group import TargetGroup, TargetGroupSchema


route_path_general = Blueprint("route_path_general", __name__)


@route_path_general.route('/target_groups', methods=['GET'])
def get_target_group_list():
    fetched = TargetGroup.query.all()
    target_group_schema = TargetGroupSchema(many=True, only=['id', 'name', 'date_created', 'external_id'])
    target_groups, error = target_group_schema.dump(fetched)
    return response_with(resp.SUCCESS_200, value={"target_groups": target_groups})


# Public API responding to the following requests
# 5 - GET target_groups/:country_code
@route_path_general.route('/target_groups/<int:country_code>', methods=['GET'])
def get_target_groups_by_country(country_code):
    fetched = Country.query.filter_by(country_code=country_code).first()
    country_schema = CountrySchema()
    country, error = country_schema.dump(fetched)
    return response_with(resp.SUCCESS_200, value={"country": country})
