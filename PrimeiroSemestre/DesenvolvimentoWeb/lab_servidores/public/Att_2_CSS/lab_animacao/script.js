let retangulo = {

    x: 50,
    y: 50,
    largura: 30,
    altura: 30,

    desenha:function()
    {
        ctx.beginPath();
        ctx.strokeStyle = "black";
        ctx.fillStyle = "red";
        ctx.strokeRect(this.x, this.y, this.largura, this.altura);
        ctx.fillRect(this.x, this.y, this.largura, this.altura);
        ctx.closePath();
    }

}


let canvas = document.getElementById("animacao");
let ctx = canvas.getContext("2d");

retangulo.desenha();

function animacao(){

    ctx.clearRect(0,0,400,400);

     if(retangulo.x < 0)
    {
        retangulo.x = 0;
    }
    if(retangulo.x > 270)
    {
        retangulo.x = 270;
    }
    if(retangulo.y < 0)
    {
        retangulo.y = 0;
    }
    if(retangulo.y >270)
    {
        retangulo.y = 270;
    }


    retangulo.desenha();
    requestAnimationFrame(animacao);
    

}

document.addEventListener("mousemove", function(evento){

        rect = canvas.getBoundingClientRect();
        x_mouse = evento.clientX - rect.left - 15;
        y_mouse = evento.clientY - rect.top - 15;
        console.log(x_mouse,y_mouse);


       
        retangulo.x = x_mouse;
        retangulo.y = y_mouse;

});

animacao();