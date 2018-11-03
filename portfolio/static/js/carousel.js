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