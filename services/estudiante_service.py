"""
Servicio para el modelo Estudiante.
Aquí se maneja la lógica de negocio relacionada con estudiantes.
"""

from repositories.estudiante_repository import EstudianteRepository
import logging

logger = logging.getLogger(__name__)

class EstudianteService:

    @staticmethod
    def create_estudiante(nombre, carrera):
        from models.db import db
        logger.info(f'Creando estudiante en servicio: {nombre}')

        estudiante = EstudianteRepository.create_estudiante(nombre, carrera, db.session)

        logger.info(f'Estudiante creado en servicio: {estudiante.nombre} (ID: {estudiante.id})')
        return estudiante

    @staticmethod
    def get_estudiante_by_id(estudiante_id):
        from models.db import db
        logger.info(f'Buscando estudiante por ID en servicio: {estudiante_id}')

        estudiante = EstudianteRepository.get_by_id(estudiante_id, db.session)
        if not estudiante:
            logger.warning(f'Estudiante no encontrado en servicio: {estudiante_id}')
        return estudiante

    @staticmethod
    def get_all_estudiantes():
        from models.db import db
        logger.info('Obteniendo todos los estudiantes en servicio')

        estudiantes = EstudianteRepository.get_all(db.session)

        logger.info(f'{len(estudiantes)} estudiantes obtenidos en servicio')
        return estudiantes

    @staticmethod
    def update_estudiante(estudiante_id, nombre, carrera):
        from models.db import db
        logger.info(f'Actualizando estudiante en servicio: {estudiante_id}')

        estudiante = EstudianteRepository.update_estudiante(estudiante_id, nombre, carrera, db.session)

        if estudiante:
            logger.info(f'Estudiante actualizado en servicio: {estudiante_id}')
        else:
            logger.warning(f'No se encontró estudiante para actualizar en servicio: {estudiante_id}')

        return estudiante

    @staticmethod
    def delete_estudiante(estudiante_id):
        from models.db import db
        logger.info(f'Eliminando estudiante en servicio: {estudiante_id}')

        success = EstudianteRepository.delete_estudiante(estudiante_id, db.session)

        if success:
            logger.info(f'Estudiante eliminado en servicio: {estudiante_id}')
        else:
            logger.warning(f'No se encontró estudiante para eliminar en servicio: {estudiante_id}')

        return success
