"""
Repositorio para el modelo Student.
Maneja las operaciones de acceso a datos para estudiantes.
"""

from sqlalchemy.orm import Session
from models.student import Student
import logging

logger = logging.getLogger(__name__)

class StudentRepository:
    @staticmethod
    def create_student(nombre, email, session: Session):
        logger.info(f'Creando estudiante en repositorio: {nombre}')
        student = Student(nombre=nombre, email=email)
        session.add(student)
        session.commit()
        logger.info(f'Estudiante creado en repositorio: {student.id} - {student.nombre}')
        return student

    @staticmethod
    def get_all(session: Session):
        logger.info('Obteniendo todos los estudiantes en repositorio')
        students = session.query(Student).all()
        logger.info(f'{len(students)} estudiantes obtenidos en repositorio')
        return students

    @staticmethod
    def get_by_id(student_id, session: Session):
        logger.info(f'Buscando estudiante con ID: {student_id}')
        return session.query(Student).filter_by(id=student_id).first()
