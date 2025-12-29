from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from config import Config
from models import db
from routes import api_bp

app = Flask(__name__)
app.config.from_object(Config)

# Init extensions
db.init_app(app)
JWTManager(app)
CORS(app)

# Register routes
app.register_blueprint(api_bp, url_prefix='/api')

if __name__ == '__main__':
    with app.app_context():
        db.create_all() # Buat tabel otomatis jika belum ada
    app.run(debug=True, port=5000)