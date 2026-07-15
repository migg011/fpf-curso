document.addEventListener('DOMContentLoaded', function () {

    const table = document.getElementById('table').querySelector('tbody');

    function addRow(id, name, username, email) {

        const newRow = table.insertRow();

        const idCell = newRow.insertCell(0);
        const nameCell = newRow.insertCell(1);
        const usernameCell = newRow.insertCell(2);
        const emailCell = newRow.insertCell(3);

        idCell.textContent = id;
        nameCell.textContent = name;
        usernameCell.textContent = username;
        emailCell.textContent = email;
    }

    function renderData(data) {
        data.forEach(user => {
            addRow(user.id, user.name, user.username, user.email)
        })
    }


    fetch('https://jsonplaceholder.typicode.com/users')
    .then(response => response.json())
    .then(data => renderData(data))
    .catch(error => console.error('Erro:', error))


});