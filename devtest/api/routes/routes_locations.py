#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import request

from api.models.model_panel_provider import PanelProvider, PanelProviderSchema
from api.utils.responses import response_with
from api.utils import responses as resp
from api.models.model_country import Country
from api.models.model_location import Location, LocationSchema, location_groups
from api.models.model_location_group import LocationGroup


route_path_general = Blueprint("route_path_general", __name__)


@route_path_general.route('/locations', methods=['GET'])
def get_location_list():
    fetched = Location.query.all()
    location_schema = LocationSchema(many=True, only=['id', 'name', 'date_created', 'date_updated', 'external_id'])
    locations, error = location_schema.dump(fetched)
    return response_with(resp.SUCCESS_200, value={"locations": locations})


# Public API responding to the following requests
# 4 - GET locations/:country_code
@route_path_general.route('/locations/<int:country_code>', methods=['GET'])
def get_locations_by_country(country_code):
    location_group = LocationGroup.query.filter_by(country_code=Country.query.filter_by(country_code=country_code))

    fetched = Location.query.filter(Location.location_groups.any(id=location_group.id)).all()

    location_schema = LocationSchema()
    result_locations, error = location_schema.dump(fetched)
    return response_with(resp.SUCCESS_200, value={"locations": result_locations})


# It should return locations which belong to the selected country
# based on it's current panel provider
@route_path_general.route('/locations/<int:panel_provider>', methods=['GET'])
def get_locations_by_panel_provider(panel_provider):
    location_group = LocationGroup.query.filter_by(panel_provider_id=panel_provider)

    fetched = Location.query.filter(Location.location_groups.any(id=location_group.id)).all()

    location_schema = LocationSchema()
    result_locations, error = location_schema.dump(fetched)
    return response_with(resp.SUCCESS_200, value={"locations": result_locations})
