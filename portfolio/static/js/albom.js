function active(id){
    /*
    Первый закомментированный вариант предоставляет изменение класса у изображения,
    на которое нажали с проверкой на содержание специфического класса только у 1 элемента.
    Минус в том, что при нажатии элемента он открывается у себя же, а не представляется первым.
    Во втором случае происходит замена src в теге изображения. Но минус в том, что можно перемещать
    миниатюры изображений местами.

    */

    /*
    var ul = document.getElementById('albom');
    var img = ul.getElementsByTagName('img');
    for(var i=0; i < img.length; i++){
        if(img[i].classList.contains('active-img')){
            img[i].classList.remove('active-img');
            img[i].classList.add('non-active-img');
        }
    }

    var listElem = document.getElementById(id);

    if (listElem.classList.contains('non-active-img')){
        listElem.classList.remove('non-active-img');
        listElem.classList.add('active-img');
    }
    else {
        listElem.classList.remove('active-img');
        listElem.classList.add('non-active-img');
    }
    */

    var elem = document.getElementById(id);
    var firstElem = document.getElementById('i0');
    var temp = elem.src;
    elem.src = firstElem.src;
    firstElem.src = temp;
}