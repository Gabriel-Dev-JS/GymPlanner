document.addEventListener("DOMContentLoaded", () => {
    const tbody = document.querySelector("tbody");

    const url = window.location.pathname;
    const idProfessor = url.split("/").pop();

    fetch(`/api/alunos/${idProfessor}`)
        .then(response => {
            return response.json();
        })
        .then(data => {
            tbody.innerHTML = "";

          
            data.forEach(aluno => {
                const row = document.createElement("tr");

                row.innerHTML = `
                    <td>${aluno[0]}</td>
                    <td>${aluno[1]} ${aluno[2]}</td> 
                    <td>
                        <a href="#" class="btn btn-primary btn-sm">Editar</a>
                        <a href="#" class="btn btn-danger btn-sm">Excluir</a>
                    </td>
                `;

                tbody.appendChild(row);
            });
        })
        .catch(error => {
            console.error(error);
        });
});
