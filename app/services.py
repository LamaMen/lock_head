from app import DAO_classes


class TechTaskService:
    def addTask(self, task_id):
        if task_id is not None:
            DAO_classes.TechTaskDAO.create(task_id)

    def deleteTask(self, task_id):
        DAO_classes.TechTaskDAO.delete(task_id)