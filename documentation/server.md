## Работа с клиентской частью
Для обращения к серверу необходимо узнать его **IP адрес в локальной подсети** и перейти по нему с **портом 5000**. 
### Главная страница
Главная страница представляет собой список доступных ячеек:
![alt text](./images/main.png)
Выпадающий список позволяет выбрать существующую задачу. Для этого надо **выбрать задачу** и **нажать на кнопку сохранения** (первая). Вторая кнопка позволяет открыть соответствующую ячейку. 
Для получения данной страницы в файле `views/views.py` определена функция:
```python
@app.route('/')
def boxes():
 return render_template('index.html', boxes=BoxService.show_all(), tasks=TechTaskService.show_all())
```
Для отображения в папке `app/templates` создан шаблон `index.html`, который принимает на вход два списка: **список ячеек** и **список существующих задач**. Главное место в шаблоне это:
```html
{% for box in boxes %}
    <div class="container-fluid">
        <div class="row">
            <div class="col-md-3 "></div>
            <div class="col-md-1 left" align="center">{{ box.box_id }}</div>
            <div class="col-md-4">
                <form action="/box/change" id="task_change{{ box.box_id }}" method="post">
                    <select name="task" class="form-control" align="center">
                        <option selected
                                value="{{ box.box_id }} - {{ box.tech_task_id }}">{{ box.tech_task_id }} </option>
                        <option value="{{ box.box_id }} - none">---</option>
                        {% for task in tasks %}
                            <option value="{{ box.box_id }} - {{ task.tech_task_id }}">{{ task.tech_task_id }}</option>
                        {% endfor %}
                    </select>
                </form>
            </div>
            <div class="col-md-1 right" align="center">
                <div>
                    <button type="submit" form="task_change{{ box.box_id }}" class="btn btn-circle">
                        <img src="{{ url_for('static', filename='save.svg') }}"
                             width="20"
                             height="20">
                    </button>
                    <button type="button" class="btn btn-circle" id="{{ box.box_id }}"><img id="{{ box.box_id }}" src="{{ url_for('static', filename='lock.svg') }}"
                                                                      width="20" height="20"></button>
                </div>
            </div>
        </div>
    </div>
    <br>
{% endfor %}
```
Тут как раз и генерируются ячейки. **Ознакомиться с данной технологией можно [тут](https://habr.com/ru/post/346340/).**

После нажатия на копку сохранения, на сервер отправляется **POST запрос** с содержимым формы. Для обработки этого события есть функция `change_box()`:
```python
@app.route('/box/change', methods=['POST'])
def change_box():
    BoxService.save(request.form.get('task'))
    return redirect('/', code=302)
```
Данная функция перенаправляет содержимое формы в класс, отвечающий за работу с ячейками. Его описание находится **ниже**.

После нажатия на кнопку открытия ячейки, отрабатывает следующий скрипт (`app/static/index.js`):
```javascript
document.body.addEventListener("click", function (event) {
    console.log("Clicked", event.target.id);
    let url = '/box/open/' + event.target.id;
    let xhr = new XMLHttpRequest();
    xhr.open('GET', url, false);
    xhr.send();
});
```
Для обработки этих запросов есть функция `open_slot_debug`:
```python
@app.route('/box/open/<box_id>')
def open_slot_debug(box_id):
    app.logger.info(box_id)
    open_slot(int(box_id))
    return redirect('/', code=302)
```
Данная функция **достаёт из url** запроса **id ячейки** и **открывает** ячейку с данным номером. Описание работы функции `open_slot()` находится [тут](./devices.md).
### Страница задач
![alt text](./images/add_task.png)
На данной странице можно добавлять новые задачи. Для добавления необходимо нажать на кнопку **сохранить**. Для удаления задачи можно нажать на красную кнопку у соответствующей задачи.

Данная страница управляется JavaScript. Данная функция обновляет список задач:
```javascript
function getTasks() {

    let url = '/tasks/list';
    let xhr = new XMLHttpRequest();
    xhr.open('GET', url, false);
    xhr.send();
    let tasks = JSON.parse(xhr.response);
    console.log(tasks)

    let tasksView = document.getElementById('tasks');
    tasksView.innerHTML = '';

    for (let i = 0; i < tasks.length; i++) {
        let title = tasks[i].title;

        tasksView.innerHTML +=
            `<div class="card mb-3">
        <div class="card-body">
        <div class="row">
          <div class="col-sm-6 text-left">
            <p>${title}</p>
          </div>
          <div class="col-sm-6 text-right">
            <a href="#" onclick="deleteTask('${title}')" class="btn btn-danger ml-5">X</a>
          </div>
        </div>  
       </div>
      </div>`;
    }
}
```
Для обновления делается запрос по адресу `/tasks/list` и сервер отправляет все доступные заказы.  Потом скрипт проходится по всем задачам и отображает их на странице.
На  стороне сервера обработка запроса выглядит следующим образом:
```python
@app.route('/tasks/list', methods=['GET'])
def get_tasks():
    tasks_json = []
    for task in TechTaskService.show_all():
        tasks_json.append({"title": task.tech_task_id})

    return jsonify(tasks_json)
```
Происходит забор данных из базы данных и отправляется полученных список обратно в формате *Json*.

Для удаления выполняется данный участок скрипта:
```javascript
function saveTask(e) {
    let title = document.getElementById('title').value;
    let url = '/tasks/add/' + title;
    let xhr = new XMLHttpRequest();
    xhr.open('GET', url, false);
    xhr.send();
    console.log(xhr.responseText);
    getTasks();
	
    document.getElementById('form-Task').reset();
    e.preventDefault();
}
```
Данная функция находит объект с **id = title** и отправляет его на сервер. Для этого делается запрос по адресу `/tasks/add/<title>` где `<title>` это значение поля ввода.
Данные запросы обрабатываются данной функцией:
```python
@app.route('/tasks/add/<task_id>')
def add_task(task_id):
    TechTaskService.add_task(task_id)
    return "Create task " + str(task_id)
```
То есть функция обрезает последнее слово в запросе и сохраняет его в базе данных.

Для удаления выполняется следующая часть скрипта:
```javascript
function deleteTask(title) {
    let url = '/tasks/delete/' + title.substring(0, title.length - 3);
    let xhr = new XMLHttpRequest();
    xhr.open('GET', url, false);
    xhr.send();
    console.log(xhr.responseText);
    getTasks();
}
```
Данная функция получает объект, у которого была нажата кнопка и отправляет запрос на его удаление. Для этого делается запрос по адресу `/tasks/delete/<title>` где `<title>` это значение полученное как аргумент.
Данные запросы обрабатываются данной функцией:
```python
@app.route('/tasks/delete/<task_id>')
def delete_task(task_id):
    TechTaskService.delete_task(task_id)
    return "Deleted task " + str(task_id)
```
Происходит действие аналогичное сохранению, только запись в бд удаляется.
### Страница логов
![alt text](./images/log.png)
Действия по генерации данной страницы аналогичны выводу списка ячеек: при запросе на определенный адрес, берётся шаблон `log.html`  и заполняется списком логов, которые получены из базы данных. 