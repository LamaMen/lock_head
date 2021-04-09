from database_setup import Box, TechTask, Log, session


class BoxDAO:
    def create(self, box_id, task_id):
        add_box = Box(box_id=box_id, tech_task_id=task_id)
        session.add(add_box)
        session.commit()

    def read_all(self):
        all_boxes = session.query(Box).all()
        session.commit()
        return all_boxes

    def update(self, box_id, task_id):
        updating_box = session.query(Box).filter_by(box_id=box_id).one()
        updating_box.tech_task_id = task_id
        session.add(updating_box)
        session.commit()

    def delete(self, box_id):
        deleting_box = session.query(Box).filter_by(box_id=box_id).one()
        session.delete(deleting_box)
        session.commit()


class TechTaskDAO:
    def create(self, task_id, number):
        add_task = TechTask(tech_task_id=task_id, number=number)
        session.add(add_task)
        session.commit()

    def read_all(self):
        all_tech_tasks = session.query(TechTask).all()
        session.commit()
        return all_tech_tasks

    def update(self, task_id):
        updating_task = session.query(TechTask).filter_by(tech_task_id=task_id).one()
        updating_task.tech_task_id = task_id
        session.add(updating_task)
        session.commit()

    def delete(self, task_id):
        deleting_task = session.query(TechTask).filter_by(tech_task_id=task_id).one()
        session.delete(deleting_task)
        session.commit()


class LogDAO:
    def create(self, log_id, worker, date, tech_task_id):
        add_log = Log(log_id=log_id, worker=worker, date=date, tech_task_id=tech_task_id)
        session.add(add_log)
        session.commit()

    def read_all(self):
        all_logs = session.query(Log).all()
        session.commit()
        return all_logs

    def update(self, log_id, worker, date, tech_task_id):
        updating_task = session.query(TechTask).filter_by(tech_task_id=tech_task_id).one()
        updating_task.tech_task_id = tech_task_id
        session.add(updating_task)
        session.commit()

    def delete_all(self, log_id, worker, date, tech_task_id):
        deleting_task = session.query(TechTask).filter_by(tech_task_id=tech_task_id).all()
        session.delete(deleting_task)
        session.commit()

    def delete_one(self, log_id, worker, date, tech_task_id):
        deleting_task = session.query(TechTask).filter_by(tech_task_id=tech_task_id).one()
        session.delete(deleting_task)
        session.commit()
