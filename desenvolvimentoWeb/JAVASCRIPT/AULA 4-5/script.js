fetch("https://jsonplaceholder.typicode.com/posts")
.then(response => response.json())
.then(data => console.log(data))
.catch(error => console.error('Erro:', error));

document.addEventListener('DOMContentLoaded', function() {
    const selectElement = document.querySelector('#mySelect');
    
    const options = [
        { value: '1', text: 'Opção 1' },
        { value: '2', text: 'Opção 2' },
        { value: '3', text: 'Opção 3' },
    ];

    options.forEach(option => {
        const optionElement = document.createElement('option');
        optionElement.value = option.value;
        optionElement.textContent = option.text;
        selectElement.appendChild(optionElement);
    });

});