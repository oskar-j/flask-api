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


route_path_panels = Blueprint("route_path_panels", __name__)


@route_path_panels.route('/panels', methods=['GET'])
def get_panel_providers_list():
    fetched = PanelProvider.query.all()
    location_schema = PanelProviderSchema(many=True, only=['id', 'code', 'date_created', 'date_updated'])
    panels, error = location_schema.dump(fetched)
    return response_with(resp.SUCCESS_200, value={"panels": panels})
