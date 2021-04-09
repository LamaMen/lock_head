from flask import jsonify, render_template

from app import app
from dao.tech_task_dao import TechTaskDAO


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/add', methods=['GET'])
def get_tasks():
    tasks = []
    for task in TechTaskDAO.read_all():
        tasks.append(task.tech_task_id)

    return jsonify({"tasks": tasks})


@app.route('/add/<task_id>')
def add_task(task_id):
    TechTaskDAO.create(task_id)
    return "Create task " + str(task_id)
