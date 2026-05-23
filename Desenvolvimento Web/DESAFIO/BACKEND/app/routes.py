from flask import Blueprint,request

from app.models import Task
from .extensions import db

tasks_bp = Blueprint('tasks', __name__)

@tasks_bp.get('/tasks')
def list_tasks():
    tasks = Task.query.order_by(Task.created_at.desc()).all()
    return {'tasks': [task.to_dict() for task in tasks]}

@tasks_bp.post('/tasks')
def create_task():
    data = request.get_json(silent=True) or {}
    title = data.get('title')
    description = data.get('description','')

    if not title:
        return {'error': 'title is required'}, 400

    task = Task(title=title, description=description)
    db.session.add(task)
    db.session.commit()
    return task.to_dict(), 201
