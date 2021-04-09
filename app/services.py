from app.DAO_classes import TechTaskDAO


class TechTaskService:
    def addTask(self, task_id):
        if task_id is not None:
            TechTaskDAO.create(task_id)

    def deleteTask(self, task_id):
        TechTaskDAO.delete(task_id)
