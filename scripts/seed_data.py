"""
Script para agregar datos de ejemplo a la base de datos SQLite.
Incluye usuarios, estudiantes y horarios.
Ejecuta este archivo para poblar las tablas iniciales.
"""

import os
from flask import Flask
from dotenv import load_dotenv
from werkzeug.security import generate_password_hash

from models.db import db
from models.user import User
from models.student import Student
from models.schedule import Schedule

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///flaskapi.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

usuarios = [
    {"username": "admin", "password": "admin123"},
    {"username": "profesor", "password": "profesor123"},
    {"username": "estudiante", "password": "estudiante123"}
]

estudiantes = [
    {"nombre": "Juan Pérez", "email": "juan.perez@example.com"},
    {"nombre": "Ana Gómez", "email": "ana.gomez@example.com"},
    {"nombre": "Carlos López", "email": "carlos.lopez@example.com"}
]

horarios = [
    {"student_id": 1, "materia": "Matemáticas", "hora_inicio": "08:00", "hora_fin": "10:00", "dia": "Lunes"},
    {"student_id": 1, "materia": "Historia", "hora_inicio": "10:00", "hora_fin": "12:00", "dia": "Martes"},
    {"student_id": 2, "materia": "Física", "hora_inicio": "09:00", "hora_fin": "11:00", "dia": "Lunes"},
    {"student_id": 3, "materia": "Inglés", "hora_inicio": "11:00", "hora_fin": "13:00", "dia": "Miércoles"}
]

with app.app_context():
    db.create_all()

    # Poblar usuarios
    for u in usuarios:
        if not User.query.filter_by(username=u["username"]).first():
            user = User(username=u["username"], password=generate_password_hash(u["password"]))
            db.session.add(user)

    # Poblar estudiantes
    for s in estudiantes:
        if not Student.query.filter_by(email=s["email"]).first():
            student = Student(nombre=s["nombre"], email=s["email"])
            db.session.add(student)

    db.session.commit()

    # Poblar horarios
    for h in horarios:
        if not Schedule.query.filter_by(student_id=h["student_id"], materia=h["materia"]).first():
            schedule = Schedule(
                student_id=h["student_id"],
                materia=h["materia"],
                hora_inicio=h["hora_inicio"],
                hora_fin=h["hora_fin"],
                dia=h["dia"]
            )
            db.session.add(schedule)

    db.session.commit()

print("Usuarios, estudiantes y horarios agregados correctamente.")
