/* let nome = prompt("Digite seu nome: ");
let idade = parseInt(prompt("Digite sua idade: "));
let ano_atual = 2024;
let ano_nascimento = ano_atual - idade;



let resposta = "Olá  " + nome + ", seu ano de nascimento é " + ano_nascimento;

document.getElementById("element").innerHTML = resposta;
 // o innerHtml trocou o parágrafo anterior para "super teste"

 */


 function alerta() //function é a palavra chave, alerta é o nome função
{

    window.alert("Alerta");
}

function alerta2(texto)
{
    window.alert(texto);
}

function soma(a,b)
{
    return a+b;//retornando valores
}

function multiplica(a,b)
{
    return a*b;
}

function ex4()
{
    let num1 = parseInt(document.getElementById("num1").value);
    let num2 = parseInt(document.getElementById("num2").value);
    let resultado = 0;

    if(num1<0 || num2<0)
    {
        resultado = soma(num1,num2);
    }
    else
    {
        resultado = multiplica(num1,num2);
    }

    document.getElementById("resultado_do_ex4").innerHTML = resultado;

}

function imprime_nome()
{

    let nome = document.getElementById("nome").value;
    console.log(nome);
} 

function multiplica_3()
{

    let valor = document.getElementById("numero").value;
    let resultado = valor*3;
    document.getElementById("resultado").innerHTML = resultado;

}

function soma2()
{
    let valor1 = parseInt(document.getElementById("n1").value);
    let valor2 = parseInt(document.getElementById("n2").value);
    let resultado = soma(valor1, valor2);
    document.getElementById("resultado_soma").innerHTML = resultado;
}

/* alerta(); //chamando função
alerta();
alerta();

mensagem = prompt("Digite um texto: ");
alerta2(mensagem); //passando parâmetro pra função */


//console.log(soma(4,5));
