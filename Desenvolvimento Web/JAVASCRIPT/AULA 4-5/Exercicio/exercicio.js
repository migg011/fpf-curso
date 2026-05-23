document.getElementById('myForm').addEventListener('submit', function(event) {
    
    event.preventDefault();

    const name = document.getElementById('name').value;
    const age = document.getElementById('age').value;


    const data = {
        name: name,
        age: age
    };

    fetch('https://jsonplaceholder.typicode.com/posts', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })

    .then(response => response.json())
    .then(data => {
        console.log("sucesso:", data);
        document.getElementById('response').textContent = "Dados enviados com sucesso: " + JSON.stringify(data);
    })
    .catch(error => {
        console.error('Erro:', error);
        document.getElementById('response').textContent = "Erro ao enviar dados";
    });
});