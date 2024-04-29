//incluindo módulos http e express
var http = require('http');
var express = require('express');
var bodyParser = require("body-parser");

const MongoClient = require("mongodb").MongoClient;
const url = `mongodb+srv://gDias:guguinha14@gsantana.sbnjkdr.mongodb.net/?retryWrites=true&w=majority&appName=GSantana`
const client = new MongoClient(url, {useNewUrlParser: true});

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
//ip:80/Home.html


//------------------------------------------------//

app.post("/cadastra", function(requisicao, resposta)
{
    user = requisicao.body.user;
    password = requisicao.body.password;
    let mensagem = `Cadastrado com sucesso!`
    //console.log(user+password);
    resposta.render(`cadastro.ejs`, {mensagem});
})

app.post("/login", function(requisicao, resposta)
{
    usuario = requisicao.body.usuario;
    senha = requisicao.body.senha;

    if(usuario === user && senha === password)
    {
        let mensagem = `Sucesso!`;
        //console.log(`Sucesso!\nUsuário:${usuario}`);
        
        resposta.render(`resposta.ejs`, {mensagem, usuario} );
    }
    else
    {
        let mensagem = `Falhou!`
        //console.log(`Falha!\nUsuário: teste`);
        resposta.render(`resposta.ejs`, { mensagem , usuario});
    }

})

app.get("/", function(requisicao, resposta)
{
    resposta.redirect("Project.html")
})

app.post("/cadastrar_usuario", function(requisicao, resposta)
{
    client.db("GSantana").collection("usuarios").insertOne(
        { db_nome: requisicao.body.nome, 
            db_login: requisicao.body.login,
            db_senha: requisicao.body.senha 

        },
        function (err) {
        if (err) {
          resposta.render('resposta', {mensagem: "Erro ao cadastrar usuário!"})
        }else {
          resposta.render('resposta', {mensagem: "Usuário cadastrado com sucesso!"})       
        };
      });
});


app.post("/logar_usuario", function(requisicao, resposta) {

    // busca um usuário no banco de dados
    client.db("GSantana").collection("usuarios").find(
      {db_login: requisicao.body.login,
        db_senha: requisicao.body.senha
     }).toArray(function(err, items) {
        console.log(items);
        if (items.length == 0) {
          resposta.render('resposta', {mensagem: "Usuário/senha não encontrado!"})
        }else if (err) {
          resposta.render('resposta', {mensagem: "Erro ao logar usuário!"})
        }else {
          resposta.render('resposta', {mensagem: "Usuário logado com sucesso!"})       
        };
      });
 
 });
 
