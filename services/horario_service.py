from models.horario_model import Horario
from app import db

class HorarioService:
    @staticmethod
    def get_all():
        """Obtiene todos los horarios registrados"""
        return Horario.query.all()

    @staticmethod
    def get_by_id(horario_id):
        """Obtiene un horario por su ID"""
        return Horario.query.get(horario_id)

    @staticmethod
    def create(data):
        """Crea un nuevo horario"""
        nuevo_horario = Horario(
            usuario_id=data.get('usuario_id'),
            dia=data.get('dia'),
            hora_inicio=data.get('hora_inicio'),
            hora_fin=data.get('hora_fin'),
            descripcion=data.get('descripcion')
        )
        db.session.add(nuevo_horario)
        db.session.commit()
        return nuevo_horario

    @staticmethod
    def update(horario_id, data):
        """Actualiza un horario existente"""
        horario = Horario.query.get(horario_id)
        if not horario:
            return None

        horario.dia = data.get('dia', horario.dia)
        horario.hora_inicio = data.get('hora_inicio', horario.hora_inicio)
        horario.hora_fin = data.get('hora_fin', horario.hora_fin)
        horario.descripcion = data.get('descripcion', horario.descripcion)

        db.session.commit()
        return horario

    @staticmethod
    def delete(horario_id):
        """Elimina un horario por ID"""
        horario = Horario.query.get(horario_id)
        if not horario:
            return False
        db.session.delete(horario)
        db.session.commit()
        return True
