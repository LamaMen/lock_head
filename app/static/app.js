document.getElementById('form-Task').addEventListener('submit', saveTask);

// Save new To-Do
function saveTask(e) {
    let title = document.getElementById('title').value;
    let url = 'http://127.0.0.1:5000/tasks/add/' + title;
    let xhr = new XMLHttpRequest();
    xhr.open('GET', url, false);
    xhr.send();
    console.log(xhr.responseText);
    getTasks();

    // Reset form-Task
    document.getElementById('form-Task').reset();
    e.preventDefault();
}

// Delete To-Do
function deleteTask(title) {
    let url = 'http://127.0.0.1:5000/tasks/delete/' + title;
    let xhr = new XMLHttpRequest();
    xhr.open('GET', url, false);
    xhr.send();
    console.log(xhr.responseText);
    getTasks();
}

// Show To-Do List
function getTasks() {

    let url = 'http://127.0.0.1:5000/tasks/list';
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

getTasks();