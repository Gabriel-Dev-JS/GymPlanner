document.querySelector('#enviar')?.addEventListener('click', async (e) => {
    var message = "Dados incorreto"
    e.preventDefault()
    try{
        const email = document.querySelector('#email').value
        const senha = document.querySelector('#senha').value
        const data = await fetch('http://127.0.0.1:5000/login',{
            method: "POST",
            headers:{
                "content-type": "application/json"
            },
            body:JSON.stringify({email:email,senha:senha}),
        })
        const response = await data.json()
        const {id} = response
        if(id === undefined){
            mensagemErro("mensagem", message)
            throw new Error
        } 
        localStorage.setItem("token",id)
        const token = localStorage.getItem("token")
        window.location.href = `http://127.0.0.1:5000/alunos/${token}`
    }catch(error){
        console.error("error", error)
    }
})

const mensagemErro = (classe,mensagem) => {
    document.querySelector(`.${classe}`).innerHTML = mensagem
    setTimeout(() => {
        document.querySelector(`.${classe}`).innerHTML = ""
    },2000)
}