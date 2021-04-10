from app.models import TechTask
from app import db


class TechTaskDAO:
    @staticmethod
    def create(task_id):
        add_task = TechTask(tech_task_id=task_id)
        db.session.add(add_task)
        db.session.commit()

    @staticmethod
    def read_all():
        return TechTask.query.all()

    @staticmethod
    def update(task_id):
        updating_task = TechTask.query.filter_by(tech_task_id=task_id).first()
        updating_task.tech_task_id = task_id
        db.session.commit()

    @staticmethod
    def delete(task_id):
        TechTask.query.filter_by(tech_task_id=task_id).delete()
        db.session.commit()
