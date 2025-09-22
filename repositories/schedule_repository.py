"""
Repositorio para el modelo Schedule.
Maneja las operaciones de acceso a datos para horarios de estudiantes.
"""

from sqlalchemy.orm import Session
from models.schedule import Schedule
import logging

logger = logging.getLogger(__name__)

class ScheduleRepository:
    @staticmethod
    def create_schedule(student_id, materia, hora_inicio, hora_fin, dia, session: Session):
        logger.info(f'Creando horario para estudiante {student_id} - {materia}')
        schedule = Schedule(
            student_id=student_id,
            materia=materia,
            hora_inicio=hora_inicio,
            hora_fin=hora_fin,
            dia=dia
        )
        session.add(schedule)
        session.commit()
        logger.info(f'Horario creado en repositorio: {schedule.id} - {materia}')
        return schedule

    @staticmethod
    def get_by_student(student_id, session: Session):
        logger.info(f'Buscando horarios del estudiante {student_id}')
        return session.query(Schedule).filter_by(student_id=student_id).all()

    @staticmethod
    def get_all(session: Session):
        logger.info('Obteniendo todos los horarios en repositorio')
        schedules = session.query(Schedule).all()
        logger.info(f'{len(schedules)} horarios obtenidos en repositorio')
        return schedules
