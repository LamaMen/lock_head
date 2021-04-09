from app.DAO_classes import TechTaskDAO


class TechTaskService:
    def add_task(self, task_id):
        if task_id is not None:
            TechTaskDAO.create(task_id)

    def delete_task(self, task_id):
        TechTaskDAO.delete(task_id)
