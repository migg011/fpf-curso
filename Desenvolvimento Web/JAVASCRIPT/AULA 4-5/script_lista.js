document.addEventListener('DOMContentLoaded', function() {

    const ulElement = document.querySelector('#myList');

    const items = ['item 1', 'item 2', 'item 3'];

    items.forEach(item => {
        const liElement = document.createElement('li');
        liElement.textContent = item;
        ulElement.appendChild(liElement);
    });

});