from flask import Flask
from flask_jwt_extended import JWTManager
from models.user_model import db
from models.horario_model import db as horario_db
from config import Config
from routes.user_routes import user_bp
from routes.horario_routes import horario_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
JWTManager(app)

@app.route('/')
def home():
    return {"msg": "API de Gestión de Horarios lista!"}

app.register_blueprint(user_bp, url_prefix='/users')
app.register_blueprint(horario_bp, url_prefix='/horarios')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
