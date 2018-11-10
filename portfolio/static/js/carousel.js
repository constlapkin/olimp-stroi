/*
Данный скрипт содержит перменные конфигурации и две функции:
next() и prev(), - которые срабатывают, после вызова.
Данные функции отвечают за перелистывание карусели на сайте.
*/

var position = 0; // Начальная позиция карусели
var width = 220; // Ширина элемента карусели (элемент + отступы)
var count = 4; // Количество отображаемых элементов
var carousel;
var list;
var listElems;
function prev() {
    carousel = document.getElementById('carousel');
    list = carousel.querySelector('ul');
    listElems = carousel.querySelectorAll('li');
    position = Math.min(position + width * count, 0)
    list.style.marginLeft = position + 'px';
};
function next() {
    carousel = document.getElementById('carousel');
    list = carousel.querySelector('ul');
    listElems = carousel.querySelectorAll('li');
    position = Math.max(position - width * count, -width * (listElems.length - count));
    list.style.marginLeft = position + 'px';
};


window.onload = function(){

    list = document.getElementById('ul');
    var i = 1;
    var si = '';
    var t = [];
    for (i; i < (list.childNodes.length - 1) / 2 - 1; i = i + 1) {
        si = 'i' + i;
        t.push(document.getElementById(si));
    }

    var i = 1;
    var ar = 0;
    if ((list.childNodes.length - 1) / 2 - 1 >= 4) {
        ar = 4;
    }
    else if ((list.childNodes.length - 1) / 2 - 1 == 3) {
        ar = 3;
    }
    else if ((list.childNodes.length - 1) / 2 - 1 == 2) {
        ar = 2;
    }
    else if ((list.childNodes.length - 1) / 2 - 1 == 1) {
        ar = 1;
    }
    for(i = 0; i < ar; i++){
        t[i].style.display = 'block';
    }


}

/* TODO: Сделать проверку на разрешение экрана для перевода всех блоков в display: block */
function fnext() {

    list = document.getElementById('ul');
    var i = 1;
    var si = '';
    var t = [];
    for (i; i < (list.childNodes.length - 1) / 2 - 1; i = i + 1) {
        si = 'i' + i;
        t.push(document.getElementById(si));
    }
    if (t.length == 8) {
        t[0].style.display = 'none';
        t[1].style.display = 'none';
        t[2].style.display = 'none';
        t[3].style.display = 'none';
        t[4].style.display = 'block';
        t[5].style.display = 'block';
        t[6].style.display = 'block';
        t[7].style.display = 'block';
    }
    else if (t.length == 7) {
        t[0].style.display = 'none';
        t[1].style.display = 'none';
        t[2].style.display = 'none';
        t[3].style.display = 'block';
        t[4].style.display = 'block';
        t[5].style.display = 'block';
        t[6].style.display = 'block';
    }
    else if (t.length == 6) {
        t[0].style.display = 'none';
        t[1].style.display = 'none';
        t[2].style.display = 'block';
        t[3].style.display = 'block';
        t[4].style.display = 'block';
        t[5].style.display = 'block';
    }
    else if (t.length == 5) {
        t[0].style.display = 'none';
        t[1].style.display = 'block';
        t[2].style.display = 'block';
        t[3].style.display = 'block';
        t[4].style.display = 'block';
    }

}


function fprev() {

    list = document.getElementById('ul');
    var i = 1;
    var si = '';
    var t = [];
    for (i; i < (list.childNodes.length - 1) / 2 - 1; i = i + 1) {
        si = 'i' + i;
        t.push(document.getElementById(si));
    }
    if (t.length == 8) {
        t[0].style.display = 'block';
        t[1].style.display = 'block';
        t[2].style.display = 'block';
        t[3].style.display = 'block';
        t[4].style.display = 'none';
        t[5].style.display = 'none';
        t[6].style.display = 'none';
        t[7].style.display = 'none';
    }
    else if (t.length == 7) {
        t[0].style.display = 'block';
        t[1].style.display = 'block';
        t[2].style.display = 'block';
        t[3].style.display = 'block';
        t[4].style.display = 'none';
        t[5].style.display = 'none';
        t[6].style.display = 'none';
    }
    else if (t.length == 6) {
        t[0].style.display = 'block';
        t[1].style.display = 'block';
        t[2].style.display = 'block';
        t[3].style.display = 'block';
        t[4].style.display = 'none';
        t[5].style.display = 'none';
    }
    else if (t.length == 5) {
        t[0].style.display = 'block';
        t[1].style.display = 'block';
        t[2].style.display = 'block';
        t[3].style.display = 'block';
        t[4].style.display = 'none';
    }

}