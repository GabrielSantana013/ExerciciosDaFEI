//incluindo módulos http e express
var http = require('http');
var express = require('express');
var bodyParser = require("body-parser");// necessario pra usar post


//variável app que acessará todos os métodos/funções no framework express
var app = express();
app.use(bodyParser.urlencoded({extended: false})); // necessario pra usar post
app.use(bodyParser.json())// necessario pra usar post
app.set('view engine', 'ejs');
app.set('views', './views');

//definindo em qual pasta estará o conteúdo estático
app.use(express.static('./public'));

//criando o servidor
var server = http.createServer(app);

///definindo o numero de porta
server.listen(80);

//teste
console.log("server rodando");

//para acessar:
//ip+porta = 80

//--------Requisições-----------//

//req e resposta são parâmetros, query é utilizado com get e depois dele é .id
app.get("/info", function(requisicao, resposta)
{
    let nome = requisicao.query.nome;
    let sobrenome = requisicao.query.sobrenome;
    console.log(nome, sobrenome);
    resposta.redirect("get.html");
})

app.get("/", function(requisicao, resposta)
{
    resposta.redirect("formulario.html")
})

//agora usando post:

app.post("/login", function(requisicao, resposta)
{
    let login = requisicao.body.login; //ao inves de query usa body no post. 
    let senha = requisicao.body.senha; //ao inves de query usa body no post. 
    let mensagem;

    if(login === "gabas" && senha === "reidelas")
    {
         mensagem = "Sucesso ao logar";
    }
    else
    {
        mensagem = "Erro ao logar!"
        //resposta.redirect("erro.html");
    }
    resposta.render("resposta.ejs", {login,senha,mensagem});
})