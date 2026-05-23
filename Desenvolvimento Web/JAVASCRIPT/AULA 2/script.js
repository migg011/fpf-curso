function tiposDeDados() {
    const nome = 'Miguel';
    const sobrenome = 'Britou';
    let nomeCompleto1 = nome + ' ' + sobrenome;
    let nomeCompleto2 = `${nome} ${sobrenome}`;

    console.log(nome);
    console.log(sobrenome);
    console.log(nomeCompleto1);
    console.log(nomeCompleto2);

    console.log(nomeCompleto1.leght);
    console.log(nomeCompleto1.substring(4));
    console.log(nomeCompleto1.substring(4, 8));
    console.log(nomeCompleto1.charAt(4));
}

function ehMaiorDeIdade(idade) {
    if(idade >= 18){
        alert("É maior de idade!")
    } else if (idade >= 0 && idade < 18) {
        alert("É menor de idade") 
    } else {
        alert("Valor informado é inválido!!")
    }
}


