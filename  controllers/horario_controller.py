"""
Controlador para Estudiantes y Horarios.
Define los endpoints REST para gestionar estudiantes y horarios.
"""

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from services.horario_service import HorarioService
import logging

logger = logging.getLogger(__name__)

horario_bp = Blueprint("horario_bp", __name__, url_prefix="/api")


# ============================
# Estudiantes
# ============================

@horario_bp.route("/estudiantes", methods=["POST"])
def crear_estudiante():
    """
    Crear un nuevo estudiante
    ---
    tags:
      - Estudiantes
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required: [nombre, carrera]
          properties:
            nombre:
              type: string
              example: "Dylan Rodriguez"
            carrera:
              type: string
              example: "Ingeniería de Sistemas"
    responses:
      201:
        description: Estudiante creado exitosamente
    """
    data = request.get_json() or {}
    nombre = data.get("nombre")
    carrera = data.get("carrera")

    if not nombre or not carrera:
        return jsonify({"msg": "nombre y carrera son requeridos"}), 400

    try:
        estudiante = HorarioService.crear_estudiante(nombre, carrera)
        return jsonify({
            "id": estudiante.id,
            "nombre": estudiante.nombre,
            "carrera": estudiante.carrera
        }), 201
    except Exception as e:
        logger.error(f"Error creando estudiante: {str(e)}")
        return jsonify({"msg": "Error creando estudiante", "detail": str(e)}), 500


@horario_bp.route("/estudiantes", methods=["GET"])
@jwt_required(optional=True)  # si quieres hacerlo opcional o requerido
def listar_estudiantes():
    """
    Listado de estudiantes
    ---
    tags:
      - Estudiantes
    responses:
      200:
        description: Lista de estudiantes
    """
    try:
        estudiantes = HorarioService.listar_estudiantes()
        return jsonify([
            {"id": e.id, "nombre": e.nombre, "carrera": e.carrera}
            for e in estudiantes
        ]), 200
    except Exception as e:
        logger.error(f"Error listando estudiantes: {str(e)}")
        return jsonify({"msg": str(e)}), 500


@horario_bp.route("/estudiantes/<int:estudiante_id>", methods=["PUT"])
def actualizar_estudiante(estudiante_id):
    data = request.get_json() or {}
    try:
        estudiante = HorarioService.actualizar_estudiante(
            estudiante_id, data.get("nombre"), data.get("carrera")
        )
        return jsonify({
            "id": estudiante.id,
            "nombre": estudiante.nombre,
            "carrera": estudiante.carrera
        }), 200
    except Exception as e:
        return jsonify({"msg": str(e)}), 400


@horario_bp.route("/estudiantes/<int:estudiante_id>", methods=["DELETE"])
def eliminar_estudiante(estudiante_id):
    try:
        HorarioService.eliminar_estudiante(estudiante_id)
        return jsonify({"msg": "Estudiante eliminado"}), 200
    except Exception as e:
        return jsonify({"msg": str(e)}), 400


# ============================
# Horarios
# ============================

@horario_bp.route("/horarios", methods=["POST"])
def crear_horario():
    data = request.get_json() or {}
    try:
        horario = HorarioService.crear_horario(
            data["materia"], data["dia"], data["hora"], data["estudiante_id"]
        )
        return jsonify({
            "id": horario.id,
            "materia": horario.materia,
            "dia": horario.dia,
            "hora": horario.hora,
            "estudiante_id": horario.estudiante_id
        }), 201
    except Exception as e:
        return jsonify({"msg": str(e)}), 400


@horario_bp.route("/horarios", methods=["GET"])
def listar_horarios():
    try:
        horarios = HorarioService.listar_horarios()
        return jsonify([{
            "id": h.id,
            "materia": h.materia,
            "dia": h.dia,
            "hora": h.hora,
            "estudiante_id": h.estudiante_id
        } for h in horarios]), 200
    except Exception as e:
        return jsonify({"msg": str(e)}), 500


@horario_bp.route("/horarios/<int:horario_id>", methods=["PUT"])
def actualizar_horario(horario_id):
    data = request.get_json() or {}
    try:
        horario = HorarioService.actualizar_horario(
            horario_id, data.get("materia"), data.get("dia"), data.get("hora")
        )
        return jsonify({
            "id": horario.id,
            "materia": horario.materia,
            "dia": horario.dia,
            "hora": horario.hora,
            "estudiante_id": horario.estudiante_id
        }), 200
    except Exception as e:
        return jsonify({"msg": str(e)}), 400


@horario_bp.route("/horarios/<int:horario_id>", methods=["DELETE"])
def eliminar_horario(horario_id):
    try:
        HorarioService.eliminar_horario(horario_id)
        return jsonify({"msg": "Horario eliminado"}), 200
    except Exception as e:
        return jsonify({"msg": str(e)}), 400
