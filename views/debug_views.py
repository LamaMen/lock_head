from app import app
from dao.box_dao import BoxDAO
from devices.slots_handler import open_slot
from services.tech_task_service import TechTaskService


@app.route('/debug/open_slot')
def open_slot_debug():
    open_slot(1)
    return 'Slot opened!'


@app.route('/debug/init_box')
def init_box():
    TechTaskService.add_task('106-04/21')
    TechTaskService.add_task('12-04/21')
    TechTaskService.add_task('71-04/21')
    TechTaskService.add_task('47-04/21')

    BoxDAO.create(1)
    BoxDAO.update(1, '106-04/21')
    BoxDAO.create(2)
    BoxDAO.update(2, '12-04/21')
    BoxDAO.create(3)
    BoxDAO.update(3, '71-04/21')
    BoxDAO.create(4)
    BoxDAO.update(4, '47-04/21')
