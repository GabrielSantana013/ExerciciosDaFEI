let pintura = document.getElementById("pintura");
let ctx = pintura.getContext("2d");


function desenhar_quadrado(x,y,tamanho,color)
{
    ctx.beginPath();
    ctx.fillStyle = color;
    ctx.strokeStyle = color;
    ctx.strokeRect(x,y,tamanho,tamanho);
    ctx.fillRect(x,y,tamanho,tamanho);
    ctx.closePath();
}

function desenhar_linha(x1,y1,x2,y2,color)
{
    ctx.beginPath();
    ctx.lineWidth = 2;
    ctx.strokeStyle = color;
    ctx.moveTo(x1,y1);
    ctx.lineTo(x2,y2);
    ctx.stroke();
    ctx.closePath();
}

function desenhar_arco(x, y ,r, ang1, ang2, color1,color2)
{
    ctx.beginPath();
    ctx.lineWidth = 3;
    ctx.strokeStyle = color1;
    ctx.fillStyle = color2;
    ctx.arc(x,y,r,ang1,ang2,color2);
    ctx.stroke();
    ctx.fill();
    ctx.closePath();
}

function escrever(x, y, texto, color)
{
    ctx.beginPath();
    ctx.lineWidth = 1;
    ctx.fillStyle = color;
    ctx.strokeStyle = color;
    ctx.font = "30px Arial";
    ctx.strokeText(texto,x,y);
    ctx.fillText(texto,x,y);
    ctx.closePath();
    
}

//quadrados
desenhar_quadrado(0,0,60,"blue");
desenhar_quadrado(240,0,60,"red");
desenhar_quadrado(0,260,40,"yellow");
desenhar_quadrado(40,260,40,"yellow");
desenhar_quadrado(0,220,40,"yellow");
desenhar_quadrado(260,260,40,"black");
desenhar_quadrado(220,260,40,"black");
desenhar_quadrado(260,220,40,"black");
desenhar_quadrado(100,150,50,"red");
desenhar_quadrado(260,130,40,"cyan");
desenhar_quadrado(0,150,40,"cyan");
desenhar_quadrado(0,110,40,"cyan");


/* #p3 {background-color:rgba(0,0,255,0.3);} /* blue with opacity */ 

//escrita
escrever(100,50,"Canvas", "black");

//linhas
desenhar_linha(0,150,300,150,"green");
desenhar_linha(0,0,150,150,"blue");
desenhar_linha(300,0,150,150,"red");
desenhar_linha(150,150,150,300,"gray");

//circulos
desenhar_arco(150,110,15,0,2*Math.PI,"blue","cyan");
desenhar_arco(205,230,15,0,2*Math.PI,"green","yellow"); 
desenhar_arco(80,230,15,0,2*Math.PI,"green","yellow"); 
desenhar_arco(150,300,40,0,2*Math.PI,"green","cyan"); 

//arcos

desenhar_arco(150,150,65,2*Math.PI,Math.PI, "green","rgba(0,0,0,0)");
desenhar_arco(150,150,85,2*Math.PI,1.75*Math.PI, "green","rgba(0,0,0,0)");
desenhar_arco(150,150,85,1.25*Math.PI,Math.PI, "green","rgba(0,0,0,0)");

desenhar_arco(150,300,70,1.5*Math.PI,Math.PI, "green","rgba(0,0,0,0)");
desenhar_arco(150,300,55,2*Math.PI,1.5*Math.PI, "green","rgba(0,0,0,0)");
