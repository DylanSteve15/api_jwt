"""
Modelo de estudiante para SQLAlchemy.
Cada estudiante tendrá credenciales de acceso y estará relacionado con sus horarios.
Puedes crear más modelos siguiendo este ejemplo y agregarlos en la carpeta models.
"""

from models.db import db
import logging

logger = logging.getLogger(__name__)

class Student(db.Model):
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), nullable=False)
    apellido = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    # Relación con horarios (cada estudiante puede tener varios horarios)
    schedules = db.relationship('Schedule', backref='student', lazy=True, cascade="all, delete-orphan")

    def __repr__(self):
        logger.info(f'Representación de estudiante solicitada: {self.username}')
        return f'<Student {self.username}>'
