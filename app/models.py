from app import db


class Box(db.Model):
    __tablename__ = 'boxes'

    box_id = db.Column(db.Integer, nullable=False, primary_key=True)
    tech_task_id = db.Column(db.String(250), db.ForeignKey('tech_task.tech_task_id'))


class TechTask(db.Model):
    __tablename__ = 'tech_task'

    tech_task_id = db.Column(db.String(250), nullable=False, primary_key=True)

    def __repr__(self):
        return '<Task {}>'.format(self.tech_task_id)


class Log(db.Model):
    __tablename__ = 'logs'

    log_id = db.Column(db.Integer, primary_key=True)
    worker = db.Column(db.String(100))
    date = db.Column(db.DateTime, nullable=False)
    tech_task_id = db.Column(db.String(250))
