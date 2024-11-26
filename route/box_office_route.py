from flask import Blueprint
from my_project.auth.controller.box_office_controller import (
    get_all_box_office,
    get_box_office_by_id,
    create_box_office,
    update_box_office,
    delete_box_office
)

box_office_bp = Blueprint('box_office', __name__)

box_office_bp.route('/box_offices', methods=['GET'])(get_all_box_office)
box_office_bp.route('/box_offices/<int:box_office_id>', methods=['GET'])(get_box_office_by_id)
box_office_bp.route('/box_offices', methods=['POST'])(create_box_office)
box_office_bp.route('/box_offices/<int:box_office_id>', methods=['PUT'])(update_box_office)
box_office_bp.route('/box_offices/<int:box_office_id>', methods=['DELETE'])(delete_box_office)
