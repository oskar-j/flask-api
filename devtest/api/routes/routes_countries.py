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


route_path_countries = Blueprint("route_path_countries", __name__)


@route_path_countries.route('/country', methods=['POST'])
def create_country():
    try:
        data = request.get_json()
        country_schema = CountrySchema()
        country, error = country_schema.load(data)
        result = country_schema.dump(country.create()).data
        return response_with(resp.SUCCESS_200, value={"country": result})
    except Exception:
        return response_with(resp.INVALID_INPUT_422)


@route_path_countries.route('/country', methods=['POST'])
def create_location():
    try:
        data = request.get_json()
        country_schema = CountrySchema()
        country, error = country_schema.load(data)
        result = country_schema.dump(country.create()).data
        return response_with(resp.SUCCESS_200, value={"country": result})
    except Exception:
        return response_with(resp.INVALID_INPUT_422)


@route_path_countries.route('/countries', methods=['GET'])
def get_country_list():
    fetched = Country.query.all()
    country_schema = CountrySchema(many=True, only=['id', 'country_code', 'date_created'])
    countries, error = country_schema.dump(fetched)
    return response_with(resp.SUCCESS_200, value={"countries": countries})


@route_path_countries.route('/country/<string:country_code>', methods=['GET'])
def get_country_detail(country_code):
    fetched = Country.query.filter_by(country_code=country_code).first()
    country_schema = CountrySchema()
    country, error = country_schema.dump(fetched)
    return response_with(resp.SUCCESS_200, value={"country": country})
