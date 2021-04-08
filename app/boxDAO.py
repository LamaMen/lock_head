from flask import render_template
from database_setup import Boxes, TechTask, Logs, Base, session


class boxDAO(Boxes):
    def create(self, box, task):
        add_box = Boxes(box_id=box, tech_task_id=task)
        session.add(add_box)
        session.commit()

    def read_all(self):
        all_boxes = session.query(Boxes).all()
        return render_template("boxes.html", all_boxes=all_boxes)

    def update(self, box, task):
        updating_box = session.query(Boxes).filter_by(box_id=box).one()
        updating_box.tech_task_id = task
        session.add(updating_box)
        session.commit()

    def delete(self, box):
        deleting_box = session.query(Boxes).filter_by(box_id=box).one()
        session.delete(deleting_box)
        session.commit()


class ttDAO(TechTask):
    def create(self, task):
        add_task = TechTask(tech_task_id=task)
        session.add(add_task)
        session.commit()

    def read_all(self):
        all_tasks = session.query(TechTask).all()
        return render_template("tasks.html", all_tasks=all_tasks)

    def update(self, task):
        updating_task = session.query(TechTask).filter_by(tech_task_id=task).one()
        updating_task.tech_task_id = task
        session.add(updating_task)
        session.commit()

    def delete(self, task):
        deleting_task = session.query(TechTask).filter_by(tech_task_id=task).one()
        session.delete(deleting_task)
        session.commit()

class logDAO(Logs):
    def create(self, log_id, worker, date, tech_task_id):
        add_log = Logs(log_id=log_id, worker=worker, date=date, tech_task_id=tech_task_id)
        session.add(add_log)
        session.commit()

    def read_all(self):
        all_logs = session.query(Logs).all()
        return render_template("log.html", all_logs=all_logs)

    # def update(self, log_id, worker, date, tech_task_id):
    #     updating_task = session.query(TechTask).filter_by(tech_task_id=task).one()
    #     updating_task.tech_task_id = task
    #     session.add(updating_task)
    #     session.commit()

    def delete_all(self, log_id, worker, date, tech_task_id):
        deleting_task = session.query(TechTask).filter_by(tech_task_id=tech_task_id).all()
        session.delete(deleting_task)
        session.commit()

    def delete_one(self, log_id, worker, date, tech_task_id):
        deleting_task = session.query(TechTask).filter_by(tech_task_id=tech_task_id).one()
        session.delete(deleting_task)
        session.commit()
