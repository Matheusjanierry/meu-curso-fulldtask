async function buscar(){
    let buscaParametro = new URLSearchParams(window.location.search)
    let parametroId = buscaParametro.get("id")
    alert(parametroId)
    let p0rocura = await fetch("lista-produtos.json")
    let produtos = await p0rocura.json()
    let indice = null
    for(let x in produtos){
        if(produtos[x].id ==parametroId){
            indice = x
        }
    }
    alert(indice)

}
buscar()