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

document.getElementById("addExercicio").addEventListener("click", function() {
    var novoExercicio = document.createElement("div");

    novoExercicio.innerHTML = `
    <hr>
        <div class="mb-3">
            <label for="exercicio" class="form-label">Exercício</label>
            <input type="text" class="form-control" name="exercicio[]" placeholder="Exemplo: Supino Reto com Barra">
        </div>
        <div class="mb-3">
            <label for="repeticao" class="form-label">Repetição</label>
            <input type="number" class="form-control" name="repeticao[]" required>
        </div>
        <div class="mb-3">
            <label for="serie" class="form-label">Série</label>
            <input type="number" class="form-control" name="serie[]" required>
        </div>
        <div class="mb-3">
            <label for="carga" class="form-label">Carga</label>
            <input type="text" class="form-control" name="carga[]" placeholder="3 kg" required>
        </div>
    `;
    
    document.getElementById("camposExercicio").appendChild(novoExercicio);
});

document.getElementById("removeExercicio").addEventListener("click", function() {
    // Seleciona o último conjunto de campos de exercício e o remove
    var campos = document.getElementById("camposExercicio");
    if (campos.children.length > 1) {
        campos.removeChild(campos.lastElementChild);
    } else {
        alert("Você deve manter ao menos um exercício.");
    }
});
