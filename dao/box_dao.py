from app.models import Box
from app import db


class BoxDAO:
    @staticmethod
    def create(box_id):
        add_box = Box(box_id=box_id, tech_task_id=None)
        db.session.add(add_box)
        db.session.commit()

    @staticmethod
    def read_all():
        return Box.query.all()

    @staticmethod
    def update(box_id, task_id):
        updating_box = Box.query.filter_by(box_id=box_id).first()
        updating_box.tech_task_id = task_id
        db.session.commit()

    @staticmethod
    def delete(box_id):
        Box.query.filter_by(box_id=box_id).delete()
        db.session.commit()
