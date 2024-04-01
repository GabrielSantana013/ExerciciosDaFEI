/*let canvas = document.getElementById("canvas");
let ctx = canvas.getContext("2d");
*/
let desafio = document.getElementById("desafio");
let dsf = desafio.getContext("2d");

//Construção de um quadrado
//tudo só funciona entre o begin e o close 

/*
ctx.beginPath();
ctx.lineWidth = 2;
ctx.strokeStyle = 'red';
ctx.fillStyle = 'blue';
ctx.strokeRect(10,10,50,50); //(x,y,altura,largura)
ctx.fillRect(10,10,50,50); //(x,y,altura,largura)
ctx.closePath();
*/


//linhas mt doidas

/*
ctx.beginPath();
ctx.lineWidth = 2;
ctx.strokeStyle = 'red';
ctx.moveTo(0,0); //vai até a coordenada sem riscar
ctx.lineTo(100,100); //vai riscando
ctx.lineTo(100,200);
ctx.lineTo(200,200);
ctx.lineTo(200,300);
ctx.lineTo(300,300);
ctx.lineTo(300,400);
ctx.lineTo(400,400);
ctx.stroke(); //mostra o desenho na tela
ctx.closePath();
*/

//circulo

/*
ctx.beginPath();
ctx.lineWidth = 10;
ctx.strokeStyle = 'red';
ctx.fillStyle = 'blue';
ctx.arc(200, 200, 50,0,2*Math.PI);
ctx.stroke();
ctx.fill();
ctx.closePath();
*/

//escrever palavras

/*
ctx.beginPath();
ctx.lineWidth = 10;
ctx.strokeStyle = 'red';
ctx.fillStyle = 'blue';
ctx.font = "90px Arial";
ctx.strokeText("Olá", 200, 200);
ctx.fillText("Olá", 200, 200);
ctx.closePath();
*/

//desafio

//linha vermelha
dsf.beginPath();
dsf.lineWidth = 2;
dsf.strokeStyle = 'red';
dsf.moveTo(0,0);
dsf.lineTo(400,400);
dsf.stroke();
dsf.closePath();

//linha azul
dsf.beginPath();
dsf.lineWidth = 2;
dsf.strokeStyle = 'blue';
dsf.moveTo(0,400);
dsf.lineTo(400,0);
dsf.stroke();
dsf.closePath();

//linha verde

dsf.beginPath();
dsf.lineWidth = 2;
dsf.strokeStyle = 'green';
dsf.moveTo(0,200); //(x,y)
dsf.lineTo(400,200); //(x,y)
dsf.stroke();
dsf.closePath();


//quadradinho vermelho

dsf.beginPath();
dsf.lineWidth = 2;
dsf.strokeStyle = 'red';
dsf.fillStyle = 'red';
dsf.strokeRect(0,0,50,50); //(x,y,altura,largura)
dsf.fillRect(0,0,50,50);
dsf.closePath();

//quadradinho azul

dsf.beginPath();
dsf.lineWidth = 2;
dsf.strokeStyle = 'blue';
dsf.fillStyle = 'blue';
dsf.strokeRect(350,0,50,50); //(x,y,altura,largura)
dsf.fillRect(350,0,50,50);
dsf.closePath();

//quadradinho amarelo

dsf.beginPath();
dsf.lineWidth = 2;
dsf.strokeStyle = 'yellow';
dsf.fillStyle = 'yellow';
dsf.strokeRect(0,350,50,50); //(x,y,altura,largura)
dsf.fillRect(0,350,50,50);
dsf.closePath();

//quadradinho verde

dsf.beginPath();
dsf.lineWidth = 2;
dsf.strokeStyle = 'green';
dsf.fillStyle = 'green';
dsf.strokeRect(350,350,50,50); //(x,y,altura,largura)
dsf.fillRect(350,350,50,50);
dsf.closePath();

//semicirculo

dsf.beginPath();
dsf.lineWidth = 2;
dsf.strokeStyle = 'green';
dsf.arc(200, 200, 70, 2*Math.PI, Math.PI);
dsf.stroke();
dsf.closePath();

//circulo esquerda

dsf.beginPath();
dsf.lineWidth = 2;
dsf.strokeStyle = 'green';
dsf.fillStyle = 'yellow';
dsf.arc(70, 130, 20, 0, 2*Math.PI);
dsf.fill();
dsf.stroke();
dsf.closePath();

//circulo direita

dsf.beginPath();
dsf.lineWidth = 2;
dsf.strokeStyle = 'green';
dsf.fillStyle = 'yellow';
dsf.arc(330, 130, 20, 0, 2*Math.PI);
dsf.fill();
dsf.stroke();
dsf.closePath();

//escrever "desenvolvimento web"

dsf.beginPath();
dsf.lineWidth = 10;
dsf.fillStyle = 'black';
dsf.font = "28px Calibri";
dsf.fillText("Desenvolvimento Web", 73, 70);
dsf.closePath();