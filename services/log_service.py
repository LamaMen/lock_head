from dao.log_dao import LogDAO

class LogService:
    @staticmethod
    def add_log(log_id):
        if log_id is not None:
            LogDAO.create(log_id)

    @staticmethod
    def show_all_log():
        return LogDAO.read_all()

    @staticmethod
    def delete_all_log():
        LogDAO.delete_all()