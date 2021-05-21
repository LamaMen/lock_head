from app import db


class Box(db.Model):
    __tablename__ = 'boxes'

    box_id = db.Column(db.Integer, nullable=False, primary_key=True)
    tech_task_id = db.Column(db.String(250), db.ForeignKey('tech_task.tech_task_id'))


class TechTask(db.Model):
    __tablename__ = 'tech_task'

    tech_task_id = db.Column(db.String(250), nullable=False, primary_key=True)


class Log(db.Model):
    __tablename__ = 'logs'

    log_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    worker = db.Column(db.String(100))
    date = db.Column(db.DateTime, nullable=False)
    tech_task_id = db.Column(db.String(250))

    def __str__(self):
        return "Дата: %r Сотрудник: %r  Номер ТЗ: %r\n" % \
               (self.get_date(), self.worker, self.tech_task_id)

    def get_date(self):
        return self.date.strftime("%Y-%m-%d %H:%M:%S")
