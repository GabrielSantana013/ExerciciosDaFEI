//incluindo módulos http e express
var http = require('http');
var express = require('express');

//variável app que acessará todos os métodos/funções no framework express
var app = express();

//definindo em qual pasta estará o conteúdo estático
app.use(express.static('./public'));

//criando o servidor
var server = http.createServer(app);

///definindo o numero de porta
server.listen(80);

//teste
console.log("server rodando");

//para acessar:
//ip:80/Att_2_CSS/Home.html