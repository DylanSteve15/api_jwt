"""
Servicio para el modelo Horario.
Aquí se maneja la lógica de negocio relacionada con horarios.
"""

from repositories.horario_repository import HorarioRepository
import logging

logger = logging.getLogger(__name__)

class HorarioService:

    @staticmethod
    def create_horario(estudiante_id, dia, hora_inicio, hora_fin, materia):
        from models.db import db
        logger.info(f'Creando horario en servicio para estudiante ID: {estudiante_id}')

        horario = HorarioRepository.create_horario(estudiante_id, dia, hora_inicio, hora_fin, materia, db.session)

        logger.info(f'Horario creado en servicio (ID: {horario.id}) para estudiante {estudiante_id}')
        return horario

    @staticmethod
    def get_horario_by_id(horario_id):
        from models.db import db
        logger.info(f'Buscando horario por ID en servicio: {horario_id}')

        horario = HorarioRepository.get_by_id(horario_id, db.session)
        if not horario:
            logger.warning(f'Horario no encontrado en servicio: {horario_id}')
        return horario

    @staticmethod
    def get_horarios_by_estudiante(estudiante_id):
        from models.db import db
        logger.info(f'Buscando horarios por estudiante en servicio: {estudiante_id}')

        horarios = HorarioRepository.get_by_estudiante(estudiante_id, db.session)

        logger.info(f'{len(horarios)} horarios obtenidos en servicio para estudiante {estudiante_id}')
        return horarios

    @staticmethod
    def get_all_horarios():
        from models.db import db
        logger.info('Obteniendo todos los horarios en servicio')

        horarios = HorarioRepository.get_all(db.session)

        logger.info(f'{len(horarios)} horarios obtenidos en servicio')
        return horarios

    @staticmethod
    def update_horario(horario_id, dia, hora_inicio, hora_fin, materia):
        from models.db import db
        logger.info(f'Actualizando horario en servicio: {horario_id}')

        horario = HorarioRepository.update_horario(horario_id, dia, hora_inicio, hora_fin, materia, db.session)

        if horario:
            logger.info(f'Horario actualizado en servicio: {horario_id}')
        else:
            logger.warning(f'No se encontró horario para actualizar en servicio: {horario_id}')

        return horario

    @staticmethod
    def delete_horario(horario_id):
        from models.db import db
        logger.info(f'Eliminando horario en servicio: {horario_id}')

        success = HorarioRepository.delete_horario(horario_id, db.session)

        if success:
            logger.info(f'Horario eliminado en servicio: {horario_id}')
        else:
            logger.warning(f'No se encontró horario para eliminar en servicio: {horario_id}')

        return success
