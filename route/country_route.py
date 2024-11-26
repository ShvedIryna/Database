from flask import Blueprint
from my_project.auth.controller.country_controller import (
    get_all_countries,
    get_country_by_code,
    create_country,
    update_country,
    delete_country
)

country_bp = Blueprint('country', __name__)

country_bp.route('/countries', methods=['GET'])(get_all_countries)
country_bp.route('/countries/<string:country_code>', methods=['GET'])(get_country_by_code)
country_bp.route('/countries', methods=['POST'])(create_country)
country_bp.route('/countries/<string:country_code>', methods=['PUT'])(update_country)
country_bp.route('/countries/<string:country_code>', methods=['DELETE'])(delete_country)
