from app import app
from dao.box_dao import BoxDAO


@app.route('/admin/init_box')
def init_box():
    BoxDAO.create(1)
    BoxDAO.create(2)
    BoxDAO.create(3)
    BoxDAO.create(4)

    return 'success'
