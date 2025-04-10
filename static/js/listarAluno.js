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

            console.log(data)
            data.forEach(aluno => {
                const row = document.createElement("tr");

                row.innerHTML = `
                    <td>${aluno.id}</td>
                    <td>${aluno.nome} ${aluno.sobrenome}</td> 
                    <td>
                        <a href="#" class="btn btn-primary btn-sm">Ver Aluno</a>
                        <a href="#" class="btn btn-danger btn-sm">Excluir Aluno</a>
                    </td>
                `;

                tbody.appendChild(row);
            });
        })
        .catch(error => {
            console.error(error);
        });
});
