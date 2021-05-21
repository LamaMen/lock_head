# База данных
Для работы с базой дынных используется библиотека `Flask-SQLAlchemy`. 
## Сущности
Для работы с базой в приложении определены сущности. Они определены в файле `/app/models.py`. 
##### Определение сущностей
На примере сущности **Box**
```python
class Box(db.Model):
    __tablename__ = 'boxes'

    box_id = db.Column(db.Integer, nullable=False, primary_key=True)
    tech_task_id = db.Column(db.String(250), db.ForeignKey('tech_task.tech_task_id'))
```
Сущность определяется классом. Он обязательно **должен быть наследован** от `db.Model`.
В поле **\_\_tablename\_\_** прописывается таблицы, которая будет соответствовать сущности. Далее описываются поля таблицы. **db.Column** это общий класс для любой колонки. Далее **указывается** конкретный **тип колонки** и **особенности колонки**, такие как признак первичного ключа или вторичного и другие. 
**Имя колонки** при создании бд будет взято **такое же, как и имя соответствующей переменной**. 
Все остальные сущности определяются аналогично.

## Работа с бд
Для работы с бд в приложении есть три класса расположенных в папке **dao**. Пример одного из них: 
```python
from app import db
from app.models import Box


class BoxDAO:
    @staticmethod
    def create(box_id):
        add_box = Box(box_id=box_id, tech_task_id=None)
        db.session.add(add_box)
        db.session.commit()

    @staticmethod
    def create_with_task(box_id, task_id):
        add_box = Box(box_id=box_id, tech_task_id=task_id)
        db.session.add(add_box)
        db.session.commit()

    @staticmethod
    def read_all():
        return Box.query.all()

    @staticmethod
    def update(box_id, task_id):
        updating_box = Box.query.filter_by(box_id=box_id).first()
        updating_box.tech_task_id = task_id
        db.session.commit()

    @staticmethod
    def delete(box_id):
        Box.query.filter_by(box_id=box_id).delete()
        db.session.commit()


```

Для каждой операции есть соответствующая функция  в библиотеке. 
Для выполнения кого-либо запроса надо у сущности вызвать поле `query` и потом выполнить необходимую функцию, например удаление по id происходит            следующей строкой: 
```python 
Box.query.filter_by(box_id=box_id).delete()
```
В данном файле импортируется переменная `db`. Для применения изменений надо вызвать у поля **session** переменной **db** метод `commit()`.

Для создания новой строчки надо создать объект            соответствующей сущности и передать его в метод `add()` у объекта `db.session`.  

## Миграции
Для создания таблиц с СУБД необходимо выполнить миграции. 
Конфигурация подключения к бд выполнена в файле **/app/config.py**
После обновления схемы в коде необходимо обновить миграции. Для этого необходимо выполнить следующую команду в папке с проектом:
```
flask db migrate -m "boxes table"
```
Данная команда просто создает сценарий миграции. Чтобы применить изменения в базе данных, необходимо использовать команду 
```
flask db upgrade
```