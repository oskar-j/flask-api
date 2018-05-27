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


@route_path_general.route('/country', methods=['POST'])
def create_country():
    try:
        data = request.get_json()
        country_schema = CountrySchema()
        country, error = country_schema.load(data)
        result = country_schema.dump(country.create()).data
        return response_with(resp.SUCCESS_200, value={"country": result})
    except Exception:
        return response_with(resp.INVALID_INPUT_422)


@route_path_general.route('/country', methods=['POST'])
def create_location():
    try:
        data = request.get_json()
        country_schema = CountrySchema()
        country, error = country_schema.load(data)
        result = country_schema.dump(country.create()).data
        return response_with(resp.SUCCESS_200, value={"country": result})
    except Exception:
        return response_with(resp.INVALID_INPUT_422)


@route_path_general.route('/countries', methods=['GET'])
def get_country_list():
    fetched = Country.query.all()
    country_schema = CountrySchema(many=True, only=['id', 'country_code', 'date_created'])
    countries, error = country_schema.dump(fetched)
    return response_with(resp.SUCCESS_200, value={"countries": countries})


@route_path_general.route('/country/<string:country_code>', methods=['GET'])
def get_country_detail(country_code):
    fetched = Country.query.filter_by(country_code=country_code).first()
    country_schema = CountrySchema()
    country, error = country_schema.dump(fetched)
    return response_with(resp.SUCCESS_200, value={"country": country})


@route_path_general.route('/locations', methods=['GET'])
def get_location_list():
    fetched = Location.query.all()
    location_schema = LocationSchema(many=True, only=['id', 'name', 'date_created', 'external_id'])
    locations, error = location_schema.dump(fetched)
    return response_with(resp.SUCCESS_200, value={"locations": locations})


@route_path_general.route('/panels', methods=['GET'])
def get_panel_providers_list():
    fetched = PanelProvider.query.all()
    location_schema = PanelProviderSchema(many=True, only=['id', 'code', 'date_created', 'date_updated'])
    panels, error = location_schema.dump(fetched)
    return response_with(resp.SUCCESS_200, value={"panels": panels})


@route_path_general.route('/target_groups', methods=['GET'])
def get_target_group_list():
    fetched = TargetGroup.query.all()
    target_group_schema = TargetGroupSchema(many=True, only=['id', 'name', 'date_created', 'external_id'])
    target_groups, error = target_group_schema.dump(fetched)
    return response_with(resp.SUCCESS_200, value={"target_groups": target_groups})


# Public API responding to the following requests
# 4 - GET locations/:country_code
@route_path_general.route('/locations/<int:country_code>', methods=['GET'])
def get_locations_by_country(country_code):
    fetched = Country.query.filter_by(country_code=country_code).first()
    country_schema = CountrySchema()
    country, error = country_schema.dump(fetched)
    return response_with(resp.SUCCESS_200, value={"country": country})


# Public API responding to the following requests
# 5 - GET target_groups/:country_code
@route_path_general.route('/target_groups/<int:country_code>', methods=['GET'])
def get_target_groups_by_country(country_code):
    fetched = Country.query.filter_by(country_code=country_code).first()
    country_schema = CountrySchema()
    country, error = country_schema.dump(fetched)
    return response_with(resp.SUCCESS_200, value={"country": country})
