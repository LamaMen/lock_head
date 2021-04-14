import datetime

from dao.log_dao import LogDAO


class LogService:
    @staticmethod
    def add_log(worker, tech_task_id):
        LogDAO.create(worker, datetime.datetime.now(), tech_task_id)

    @staticmethod
    def show_logs():
        return LogDAO.read_all()

    @staticmethod
    def delete_logs():
        LogDAO.delete_all()

    @staticmethod
    def download_logs():
        logs = open("Logs.txt", "w")
        for log in LogService.show_all_log():
            logs.write(log.__str__())
        logs.close()
        return logs
