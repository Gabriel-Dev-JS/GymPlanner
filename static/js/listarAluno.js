document.addEventListener("DOMContentLoaded", () => {
    const tbody = document.querySelector("tbody");

    const url = window.location.pathname;
    const idProfessor = url.split("/").pop();

    fetch(`/api/listarAlunos/${idProfessor}`)
        .then(response => {
            return response.json();
        })
        .then(data => {
            tbody.innerHTML = "";

            data.forEach(aluno => {
                const row = document.createElement("tr");

                row.innerHTML = `
                    <td>${aluno.id}</td>
                    <td>${aluno.nome} ${aluno.sobrenome}</td> 
                    <td>
                        <a href="http://127.0.0.1:5000/aluno/${idProfessor}/${aluno.id}" class="btn btn-primary btn-sm">Visualizar Exercícios</a>
                        <a onClick="deletarAluno(${aluno.id})" class="btn btn-danger btn-sm">Excluir Aluno</a>
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
    const token = sessionStorage.getItem("token")
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

const deletarAluno = async (id_aluno) => {
    const token = sessionStorage.getItem("token")
    try{
        await fetch(`http://127.0.0.1:5000/listarAlunos/${token}/${id_aluno}`, {
            method:"DELETE",
            headers:{
                "content-type": "application/json"
            },
        })
        location.reload()
    }catch(error){
        console.error("Erro", error)
        throw new Error("Impossivel deletar este usuario")
    }

    // document.querySelector('pesquisarAluno')?.addEventListener('click', (e) => {
    //     e.preventDefault();
    //     const aluno = document.querySelector('#pesquisarAlunos').value
        
    // })
}
