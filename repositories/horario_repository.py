from models.horario_model import Horario
from models.db import db

class HorarioRepository:
    @staticmethod
    def get_all():
        return Horario.query.all()

    @staticmethod
    def get_by_id(horario_id):
        return Horario.query.get(horario_id)

    @staticmethod
    def delete(horario_id):
        horario = Horario.query.get(horario_id)
        if horario:
            db.session.delete(horario)
            db.session.commit()
            return True
        return False
