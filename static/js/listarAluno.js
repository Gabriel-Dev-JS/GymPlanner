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


document.querySelector("#cadastrarAluno").addEventListener("click", async (e) => {
    const token = localStorage.getItem("token")
    const url = `http://127.0.0.1:5000/listarAlunos/${token}`
    e.preventDefault();
    const emailAluno = document.getElementById("emailAluno").value
    const senhaAluno = document.getElementById("senhaAluno").value
    const nomeAluno = document.getElementById("nomeAluno").value
    const sobrenomeAluno = document.getElementById("sobrenomeAluno").value

    const formData = {
        nome: nomeAluno,
        sobrenome: sobrenomeAluno,
        email: emailAluno,
        senha: senhaAluno
    }
    
    try{
        await fetch(url,{
            method:"POST",
            headers:{
                "content-type": "application/json"
            },
            body: JSON.stringify(formData)
        })
        location.reload()
    }catch(error){
        alert('já existe um aluno com este email')
        console.error("Erro", error)
        throw new Error("Erro")
    }
})