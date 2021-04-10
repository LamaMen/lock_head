import flask
from flask import jsonify, render_template, redirect

from app import app
from dao.tech_task_dao import TechTaskDAO
from services.tech_task_service import TechTaskService


@app.route('/')
def boxes():
    return render_template('index.html')


@app.route('/tasks')
def tasks():
    return render_template('tasks.html')


@app.route('/log')
def log():
    return render_template('log.html')


@app.route('/add', methods=['GET'])
def get_tasks():
    tasks_from_db = []
    for task in TechTaskDAO.read_all():
        tasks_from_db.append(task.tech_task_id)

    return jsonify({"tasks": tasks_from_db})


@app.route('/tasks/add/<task_id>')
def add_task(task_id):
    TechTaskService.add_task(task_id)
    return redirect('/tasks')


@app.route('/tasks/delete/<task_id>')
def delete_task(task_id):
    TechTaskService.delete_task(task_id)
    return redirect('/tasks')
