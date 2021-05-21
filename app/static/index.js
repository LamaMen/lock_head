document.body.addEventListener("click", function (event) {
    console.log("Clicked", event.target.id);
    let url = '/box/open/' + event.target.id;
    let xhr = new XMLHttpRequest();
    xhr.open('GET', url, false);
    xhr.send();
});