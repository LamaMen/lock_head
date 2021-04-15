from dao.box_dao import BoxDAO


class BoxService:
    @staticmethod
    def change_task(box_id, task_id):
        BoxDAO.update(box_id, task_id)

    @staticmethod
    def show_all():
        return BoxDAO.read_all()

    @staticmethod
    def add_box():
        BoxDAO.create()

    @staticmethod
    def save(box_id, tech_task_id):
        BoxDAO.update(box_id, tech_task_id)
