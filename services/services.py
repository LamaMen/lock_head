from dao.tech_task_dao import TechTaskDAO


class TechTaskService:
    @staticmethod
    def add_task(task_id):
        if task_id is not None:
            TechTaskDAO.create(task_id)

    @staticmethod
    def delete_task(task_id):
        TechTaskDAO.delete(task_id)
