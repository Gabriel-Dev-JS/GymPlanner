document.getElementById('formExercicio').addEventListener('submit', function(event) {
    event.preventDefault();  

    const exercicio = document.getElementById('exercicio').value;
    const repeticao = document.getElementById('repeticao').value;
    const serie = document.getElementById('serie').value;
    const data = document.getElementById('data').value;
    const id_aluno = document.getElementById('id_aluno').value;

    const formData = {
        exercicio: exercicio,
        repeticao: repeticao,
        serie: serie,
        data: data,
        id_aluno: id_aluno
    };
    
    fetch('/aluno/' + id_aluno + '/exercicio', {
        method: 'POST', 
        headers: {
            'Content-Type': 'application/json',  
        },
        body: JSON.stringify(formData) 
    })
    .then(response => response.json())
    .then(data => {
        console.log('Sucesso:', data);
        alert('Exercício criado com sucesso');
    })
    .catch((error) => {
        console.error('Erro:', error);
        alert('Erro ao criar exercício');
    });
});