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

//redireciona por padrão pra página cadastroLoja
app.get("/", function(requisicao, resposta)
{
    resposta.redirect("cadastroLoja.html")
})

app.post("/cadastrar_usuario", function(req, res){

    client.db("GSantana").collection("usuarios").insertOne(
    {   db_nome: req.body.nome,
        db_login: req.body.login,
        db_senha: req.body.senha
    },
    function (err)
    {
        if(err)
        {
            res.render('respostaErro', {mensagem: "Erro ao cadastrar usuario!"})
        }
        else
        {
            res.render('respostaCadastro', {mensagem: "Usuario Cadastrado com Sucesso!"})
        };
    });
});

app.post("/logar_usuario", function(req,res){

    client.db("GSantana").collection("usuarios").findOne(
        {
            db_nome: req.body.nome,
            db_login: req.body.login,
            db_senha: req.body.senha
        },
        function(err, usuarioEncontrado)
        {
            if(err)
            {
                res.render('respostaErro', {mensagem: "Usuário/senha não encontrado!"})
            }
            else if(!usuarioEncontrado)
            {
                res.render('respostaErro', { mensagem: "Usuário/senha não encontrado!" });
            }
            else
            {
                client.db("GSantana").collection("carros").find().toArray(function(err, itens){
                res.render('respostaLogin', {mensagem: "Login Realizado com Sucesso!", carros:itens})
            })
        }
    });
});

app.post("/cadastrar_carro", function(req,res){

    client.db("GSantana").collection("carros").insertOne(
        {
            db_marca: req.body.marca,
            db_modelo: req.body.modelo,
            db_ano: req.body.ano,
            db_qtde_disponivel: req.body.qtde_disponivel
        },
        function(err)
        {
            if(err)
            {
                res.render('respostaGerenciaCarro', {mensagem: "Erro! Veículo não cadastrado"})
            }
            else
            {
                client.db("GSantana").collection("carros").find().toArray(function(err, itens){
                res.render('respostaLogin', {mensagem: "Veículo cadastrado com sucesso!", carros:itens})
                }) 
            }
        });
});

app.post("/excluir_carros", function(req, res){
      client.db("GSantana").collection("carros").deleteOne(
        {
          db_marca: req.body.marca,
          db_modelo: req.body.modelo,
          db_ano: req.body.ano
        },
        function(err, result)
        {
          if(result.deletedCount == 0)
            {
              client.db("GSantana").collection("carros").find().toArray(function(err, itens){
                res.render('respostaLogin', {mensagem:"Veículo não encontrado!", carros:itens})
              })
            }
          else if(err)
            {
              client.db("GSantana").collection("carros").find().toArray(function(err, itens){
                res.render('respostaLogin', {mensagem:"Erro ao excluir o veículo", carros:itens})
              })
            }
          else
          {
            client.db("GSantana").collection("carros").find().toArray(function(err, itens){
              res.render('respostaLogin', {mensagem:"Veículo excluído com sucesso!", carros:itens})
            })
          }
    });
});



app.post("/atualiza_carros", function(req, resp) {

  client.db("GSantana").collection("carros").updateOne(
      { db_marca: req.body.marca,
        db_modelo: req.body.modelo,
        db_ano: req.body.ano,
        db_qtde_disponivel: req.body.qtde_disponivel
      },
      { $set: 
        {db_marca: req.body.novaMarca,
          db_modelo: req.body.novoModelo,
          db_ano: req.body.novoAno,
          db_qtde_disponivel: req.body.novaQtde,
        }
      }, function (err, result) {
        if (result.modifiedCount == 0) {
          client.db("GSantana").collection("carros").find().toArray(function(err,itens){
            resp.render('respostaLogin', {mensagem: "Carro não encontrado!",carros:itens})
          })
        }else if (err) {
          client.db("GSantana").collection("carros").find().toArray(function(err,itens){
            resp.render('respostaLogin', {mensagem: "Carro não encontrado!",carros:itens})
          })
        }else {
          client.db("GSantana").collection("carros").find().toArray(function(err, itens){
          resp.render('respostaLogin', {mensagem: "Carro atualizado com sucesso!",carros:itens})       
          })
        };
  });
});

  app.post("/comprar_carro", function(req, res) {
    var dadosCarro = {
        db_marca: req.body.marca,
        db_modelo: req.body.modelo,
        db_ano: req.body.ano,
    };

    client.db("GSantana").collection("carros").findOne(dadosCarro, function(err, carros) {
        let novaQuantidade = carros.db_qtde_disponivel - 1;
        client.db("GSantana").collection("carros").updateOne(dadosCarro, {$set: {db_qtde_disponivel: novaQuantidade}}, function(err, carro)
        {
          if(carros.modifiedCount != 0 && !err)
            {
              client.db("GSantana").collection("carros").find().toArray(function(err, itens)
              {
                res.render('respostaLogin', {mensagem: "Carro comprado com sucesso!", carros: itens});
              });
            };
        });
    });
  });



/*app.post("/cadastrar_usuario", function(requisicao, resposta)
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
});*/


/*app.post("/logar_usuario", function(requisicao, resposta) {

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
 
 });*/


 /*app.post("/atualizarSenha", function(req, resp) {

  // atualiza senha do usuário
  client.db("GSantana").collection("usuarios").updateOne(
      { db_login: req.body.login, db_senha: req.body.senhaAtual },
      { $set: {db_senha: req.body.novaSenha} }, function (err, result) {
        console.log(result);
        if (result.modifiedCount == 0) {
          resp.render('respostaNovaSenha', {mensagem: "Usuário/senha não encontrado!"})
        }else if (err) {
          resp.render('respostaNovaSenha', {mensagem: "Erro ao atualizar usuário!"})
        }else {
          resp.render('respostaNovaSenha', {mensagem: "Usuário atualizado com sucesso!"})       
        };
  });

});*/


  /*app.post("/removerUsuario", function(req, resp) {

    // remove do usuário
    client.db("GSantana").collection("usuarios").deleteOne(
      { db_login: req.body.login, db_senha: req.body.senhaAtual } , function (err, result) {
        console.log(result);
        if (result.deletedCount == 0) {
          resp.render('resposta', {mensagem: "Usuário/senha não encontrado!"})
        }else if (err) {
          resp.render('resposta', {mensagem: "Erro ao remover usuário!"})
        }else {
          resp.render('resposta', {mensagem: "Usuário removido com sucesso!"})       
        };
      });
 
 });*/