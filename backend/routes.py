from flask import Blueprint, request, jsonify
from models import db, Task
from flask_jwt_extended import create_access_token, jwt_required
from datetime import datetime

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
@jwt_required()
def create_task():
    data = request.json
    
    start_date = datetime.strptime(data['start_date'], '%Y-%m-%d').date() if data.get('start_date') else None
    end_date = datetime.strptime(data['end_date'], '%Y-%m-%d').date() if data.get('end_date') else None

    new_task = Task(
        title=data['title'],
        description=data.get('description', ''),
        status=data.get('status', 'To Do'),
        start_date=start_date,
        end_date=end_date
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

    if 'start_date' in data:
        task.start_date = datetime.strptime(data['start_date'], '%Y-%m-%d').date() if data['start_date'] else None
    
    if 'end_date' in data:
        task.end_date = datetime.strptime(data['end_date'], '%Y-%m-%d').date() if data['end_date'] else None
    
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