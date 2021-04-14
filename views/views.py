from sqlite3 import Date

from flask import jsonify, render_template, send_file

from app import app
from services.log_service import LogService
from services.box_service import BoxService
from services.tech_task_service import TechTaskService


@app.route('/')
def boxes():
    # all_boxes = BoxService.show_all()
    # return render_template('tasks.html', list=all_boxes)
    return render_template('index.html')


@app.route('/tasks')
def tasks():
    # all_tasks = TechTaskService.show_all()
    # return render_template('tasks.html', list=all_tasks)
    return render_template('tasks.html')


@app.route('/log')
def log():
    # all_logs = LogService.show_all_log()
    # return render_template('log.html', list=all_logs)
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


# @app.route('/log/add')
# def add_log():
#     LogService.add_log(1, "Dima", Date.max, 123)
#     LogService.add_log(2, "Iluha", Date.max, 123)
#     return 0


@app.route('/log/download')
def logs_download():
    logs = LogService.download_logs()
    return send_file(logs)


