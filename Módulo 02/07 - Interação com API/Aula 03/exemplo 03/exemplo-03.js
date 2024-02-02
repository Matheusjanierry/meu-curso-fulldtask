async function experimentoCien(){
    let series = await fetch("series.txt")
    let convertido = await series.text()
    document.getElementById("teste01").textContent = convertido

}
experimentoCien()

async function aulaRamon(){
    let ramonlidao= await fetch("ramon.txt")
    let convertido = await ramonlidao.text()
    document.getElementById("teste02").textContent = convertido
    
}
aulaRamon()