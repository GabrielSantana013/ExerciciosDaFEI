
let resposta = Math.floor(Math.random() *100);

function guess()
{
    let palpite = parseInt(document.getElementById("num").value);

    console.log(resposta)
    console.log(palpite) 
    
    if(resposta == palpite)
    {
        document.getElementById("resposta").innerHTML = "Número correto! Parabéns!";
        document.getElementById("blocoResposta").style.setProperty("background-color","green");
    }
    else if(isNaN(palpite) == false)
    {
        if(palpite < resposta && isNaN(palpite) == false)
        {
            var menores = document.getElementById("menorQ");
            menores.innerHTML += palpite + ","
        }
        else if (palpite> resposta && isNaN(palpite) == false)
        {
            var maiores = document.getElementById("maiorQ");
            maiores.innerHTML += palpite + ","            
        }
        document.getElementById("resposta").innerHTML = "Número Errado! Tente novamente.";
        document.getElementById("blocoResposta").style.setProperty("background-color","red");
    }
    
    
}