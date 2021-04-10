import datetime

from dao.log_dao import LogDAO


class LogService:
    @staticmethod
    def add_log(worker, tech_task_id):
        LogDAO.create(worker, datetime.datetime.now(), tech_task_id)

    @staticmethod
    def show_all_log():
        return LogDAO.read_all()

    @staticmethod
    def delete_all_log():
        LogDAO.delete_all()
