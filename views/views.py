from flask import jsonify, render_template, send_file, request, redirect

from app import app
from services.log_service import LogService
from services.tech_task_service import TechTaskService
from services.box_service import BoxService


@app.route('/')
def boxes():
    return render_template('index.html', boxes=BoxService.show_all(), tasks=TechTaskService.show_all())


@app.route('/tasks')
def tasks():
    return render_template('tasks.html')


@app.route('/log')
def log():
    return render_template('log.html', logs=LogService.show_logs())


@app.route('/add', methods=['GET'])
def get_tasks():
    tasks_from_db = []
    for task in TechTaskService.show_all():
        tasks_from_db.append(task.tech_task_id)

    return jsonify({"tasks": tasks_from_db})


@app.route('/tasks/add/<task_id>')
def add_task(task_id):
    TechTaskService.add_task(task_id)
    return "Create task " + str(task_id)


@app.route('/tasks/delete/<task_id>')
def delete_task(task_id):
    TechTaskService.delete_task(task_id)
    return "Deleted task " + str(task_id)


@app.route('/log/download')
def logs_download():
    logs = LogService.download_logs()
    return send_file(logs)


@app.route('/box/change', methods=['POST'])
def change_box():
    BoxService.save(request.form.get('task'))
    return redirect('/', code=302)
