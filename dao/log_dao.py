from app import db
from app.models import Log


class LogDAO:
    @staticmethod
    def create(worker, date, tech_task_id):
        add_log = Log(worker=worker, date=date, tech_task_id=tech_task_id)
        db.session.add(add_log)
        db.session.commit()

    @staticmethod
    def read_all():
        return Log.query.all()

    @staticmethod
    def delete_all():
        Log.query.delete()
        db.session.commit()

    @staticmethod
    def delete_one(log_id):
        Log.query.filter_by(log_id=log_id).delete()
        db.session.commit()
