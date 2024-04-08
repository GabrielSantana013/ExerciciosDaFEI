let cores = [];
let cores_novas = ["preto","branco"]
console.log(cores);

cores.push("azul","verde","vermelho");

console.log(cores);
console.log(cores.length);
console.log(cores[2]);
console.log(cores.toString());

cores = cores.concat(cores_novas);
console.log(cores.toString());
console.log(cores)

let carro = {

cor:"azul",
qtdeRodas: 4,
qtdePortas: 4,
fabricante: "ford",

buzina: function()
{
    console.log("bee bee!");
},

ligarFarol: function(){

    console.log("luz");
}
}

let carro2 = {

    buzina:function()
    {
        console.log("fom fom!");
    }

}


let carros = [carro,carro2];

for(let i = 0; i <carros.length; i++)
{
    carros[i].buzina();
}


let retangulo = {

    x: 10,
    y: 20,
    largura: 50,
    altura: 50,
    cor_linha: "blue",
    cor_preenchimento: "red",

    desenha:function()
    {
        ctx.beginPath()
        ctx.strokeStyle = this.cor_linha;
        ctx.fillStyle = this.cor_preenchimento
        ctx.strokeRect(this.x,this.y,this.largura,this.altura);
        ctx.fillRect(this.x,this.y,this.largura,this.altura)
        ctx.closePath();

    }

}

let retangulo2 = {

    x: 50,
    y: 50,
    largura: 30,
    altura: 30,
    cor_linha: "blue",
    cor_preenchimento: "yellow",

    desenha:function()
    {
        ctx.beginPath()
        ctx.strokeStyle = this.cor_linha;
        ctx.fillStyle = this.cor_preenchimento
        ctx.strokeRect(this.x,this.y,this.largura,this.altura);
        ctx.fillRect(this.x,this.y,this.largura,this.altura)
        ctx.closePath();

    }

}

let canvas = document.getElementById("canvas");
let ctx = canvas.getContext("2d");

retangulo.desenha();

retangulo.x = 100;
retangulo.y = 100;

retangulo.desenha();

ctx.clearRect(0,0,400,400);

retangulo2.desenha();

retangulo2.x = 300;
retangulo2.y = 300;
retangulo2.cor_preenchimento = "green";
retangulo2.desenha();
ctx.clearRect(0,0,400,400);

let valor = 1;
// valor2 = 1;

function animacao(){

    ctx.clearRect(0,0,400,400);
    
   /* if(retangulo.x == 350)
    {
        valor = -1;
    }
    if(retangulo.x == 0)
    {
        valor = 1;
    }
*/


//retangulo.x = retangulo.x +valor;

    
    retangulo.desenha();
    retangulo2.desenha();
    requestAnimationFrame(animacao);
}

document.addEventListener("keydown", function(evento){

    tecla = evento.key;
    console.log(tecla)

    if(tecla == "ArrowUp")
    {
        retangulo2.y = retangulo2.y -3;
    }
    if(tecla == "ArrowDown")
    {
        retangulo2.y++
    }
    if(tecla == "ArrowLeft")
    {
        retangulo2.x--;
    }
    if(tecla == "ArrowRight")
    {
        retangulo2.x++;
    }

});


document.addEventListener("mousemove", function(evento){

    rect = canvas.getBoundingClientRect();
    x_mouse = evento.clientX - rect.left;
    y_mouse = evento.clientY - rect.top;
    console.log(x_mouse,y_mouse);
    retangulo.x = x_mouse;
    retangulo.y = y_mouse;

});

animacao();