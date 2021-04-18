from dao.tech_task_dao import TechTaskDAO


class TechTaskService:
    @staticmethod
    def add_task(task_id):
        if task_id is not None:
            task_id += '/21'
            TechTaskDAO.create(task_id)

    @staticmethod
    def delete_task(task_id):
        task_id += '/21'
        TechTaskDAO.delete(task_id)

    @staticmethod
    def show_all():
        return TechTaskDAO.read_all()
