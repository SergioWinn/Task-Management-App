from flask import Blueprint, request, jsonify
from models import db, Task
from flask_jwt_extended import create_access_token, jwt_required

api_bp = Blueprint('api', __name__)

# Login
@api_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    # Hardcoded credentials
    if username == 'admin' and password == 'admin123':
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    
    return jsonify({"msg": "Bad username or password"}), 401

# Create task
@api_bp.route('/tasks', methods=['POST'])
@jwt_required() # Butuh login
def create_task():
    data = request.json
    new_task = Task(
        title=data['title'],
        description=data.get('description', ''),
        status=data.get('status', 'To Do')
    )
    db.session.add(new_task)
    db.session.commit()
    return jsonify(new_task.to_dict()), 201

# Read task
@api_bp.route('/tasks', methods=['GET'])
@jwt_required()
def get_tasks():
    tasks = Task.query.all()
    return jsonify([task.to_dict() for task in tasks]), 200

# Update task
@api_bp.route('/tasks/<int:id>', methods=['PUT'])
@jwt_required()
def update_task(id):
    task = Task.query.get_or_404(id)
    data = request.json
    
    task.title = data.get('title', task.title)
    task.description = data.get('description', task.description)
    task.status = data.get('status', task.status)
    
    db.session.commit()
    return jsonify(task.to_dict()), 200

# Delete task
@api_bp.route('/tasks/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_task(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return jsonify({"msg": "Task deleted"}), 200