from flask import Blueprint
from controllers.horario_controller import get_horarios, delete_horario

horario_bp = Blueprint('horario_bp', __name__)

horario_bp.route('/', methods=['GET'])(get_horarios)
horario_bp.route('/<int:horario_id>', methods=['DELETE'])(delete_horario)
