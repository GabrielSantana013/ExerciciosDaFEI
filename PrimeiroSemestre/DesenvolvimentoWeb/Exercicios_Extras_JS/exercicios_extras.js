/*

1-A nota final de um estudante é calculada a partir de três notas atribuídas respectivamente a um trabalho de laboratório,
a uma avaliação semestral e a um exame final. A média das três notas mencionadas obedece aos pesos a seguir:

Trab lab - Peso 2
Avaliação semestral - Peso 3
Exame Final - Peso 5

Faça um programa que receba as três notas, calcule e mostre a média ponderada e o conceito, conforme tabela abaixo: 

*/

/*

let n1,n2,n3, media;

n1 = parseInt(prompt("Digite a primeira nota:"));
n2 = parseInt(prompt("Digite a segunda nota:"));
n3 = parseInt(prompt("Digite a terceira nota:"));

media = ((n1*2)+(n2*3)+(n3*5))/(2+3+5);
console.log(media);

if(media>=8 )
{
    console.log("A"); 
}

else if(media>=7 && media <8)
{
    console.log("B"); 
}

else if(media>=6 && media <7)
{
    console.log("C"); 
}

else if(media>=5 && media <6)
{
    console.log("D"); 
}

else 
{
    console.log("E");    
}

*/

/*
2- 
Faça um programa que receba quatro valores: I, A, B e C. Destes Valores, I é um valor inteiro valendo 1, 2 ou 3. 
A, B e C são valores reais. 
Escreva os números A, B e C obedecendo à tabela a seguir, dependendo do valor de I
*/

 /* let a,b,c, i;

i = parseInt(prompt("Digite o valor de I"));
while(i<=0 || i>3)
{
    i = parseInt(prompt("Digite o valor de I"));
}
a = parseFloat(prompt("Digite o valor de A"));
b = parseFloat(prompt("Digite o valor de B"));
c = parseFloat(prompt("Digite o valor de C"));

if(i == 1)
{
    
    if(a>b)
    {
        a = a+b;
        b = a-b;
        a = a-b;
    }

    if(b>c)
    {
        b = c+b;
        c = b-c;
        b = b-c;
    }

    if(a>b)
    {
        a = b+a;
        b = a-b;
        a = a-b;
    }

}

else if(i == 2)
{

    if(a<b)
    {
        a = a+b;
        b = a-b;
        a = a-b;
    }

    if(b<c)
    {
        b = c+b;
        c = b-c;
        b = b-c;
    }

    if(a<b)
    {
        a = b+a;
        b = a-b;
        a = a-b;
    }

}

else
{
    if(a>b)
    {
        a = a+b;
        b = a-b;
        a = a-b;
    }

    if(b<c)
    {
        b = c+b;
        c = b-c;
        b = b-c;
    }
    
}

console.log(a,b,c);  */


/*
3-Faça um programa que receba a altura e o peso de uma pessoa.
De acordo com a tabela a seguir, verifique e mostre qual a classificação (A, B, C, D, E, F, G, H e I) dessa pessoa.

*/

/* let altura, peso;

altura = parseFloat(prompt("Digite a altura"));
peso = parseFloat(prompt("Digite o peso"));

if(altura<1.2)
{
    if(peso<60)
    {
        console.log("A");   
    }
    else if(peso>=60 && peso <90)
    {
        console.log("D");  
    }
    else
    {
        console.log("G");  
    }
}

else if(altura>=1.2 && altura<=1.7)
{
    if(peso<60)
    {
        console.log("B");   
    }
    else if(peso>=60 && peso<90)
    {
        console.log("E");  
    }
    else
    {
        console.log("H");  
    }
}

else
{
    if(peso<60)
    {
        console.log("C");   
    }
    else if(peso>=60 && peso <90)
    {
        console.log("F");  
    }
    else
    {
        console.log("I");  
    }
} */

/*
5-Faça um programa que receba duas notas de 6 alunos,
calcule e mostre:  a média aritmética das duas notas de cada aluno;
a mensagem que está na tabela a seguir: 
*/

/* let n1, n2;

for(let i = 0; i<5; i++)
{
    n1 = parseFloat(prompt(`Digite a nota 1 do aluno ${i+1}`));
    n2 = parseFloat(prompt(`Digite a nota 2 do aluno ${i+1}`)); //toFixed(2) formata pra 2 casas decimais

    let media = n1+n2/2;

    console.log(media);

    if(media <3)
    {
        console.log("Reprovado");
    }
    else if(media <=3 && media <7)
    {
        console.log("Exame");
    }
    else
    {
        console.log("Aprovado");
    }
} */

/*
Faça um programa para calcular a área de um triângulo.
Esse programa não pode permitir a entrada de dados inválidos, ou seja, medidas menores ou iguais a 0.  
*/

/* let base, altura, area;

do {
    base = parseFloat(prompt("Digite a base:"));
} while (base <= 0)

do {
    altura = parseFloat(prompt("Digite a altura:"));
} while (altura <= 0)


area = (base * altura) / 2;

console.log(`Area: ${area.toFixed(2)}`); */

/*

7-Faça um programa que receba vários números, calcule e mostre:

A soma dos números digitados
A quantidade de números digitados
A média dos números digitados
O maior número digitado
O menor número digitado
A média dos números pares
A porcentagem dos números ímpares entre todos os números digitados.
Finalize a entrada de dados digitando a palavra “sair”

*/

let n1,somaTotal = 0, qttNum = 0, mediaNum = 0, maiorNum = 0, menorNum = 0, mediaPar = 0, numPar = 0, numImpar = 0, somaPar= 0, pctImpar= 0;

n1 = prompt("Digite um numero: ");
menorNum = parseInt(n1);

while(n1 != "sair")
{  

    somaTotal += parseInt(n1);
    qttNum++;
    mediaNum = somaTotal/qttNum;
    if(parseInt(n1)>maiorNum)
    {
        maiorNum = parseInt(n1);
    }

    if(parseInt(n1)<menorNum)
    {
        maiorNum = parseInt(n1);
    }

    if(parseInt(n1)%2===0)
    {
        somaPar += parseInt(n1);
        numPar++;
    }
    else
    {
        numImpar++;
    }

    mediaPar = somaPar/numPar;
    pctImpar = (numImpar*100)/qttNum;

    n1 = prompt("Digite um numero: ");

}

console.log(`Soma total:${somaTotal}`);
console.log(`Quantidade de numeros digitados:${qttNum}`);
console.log(`media dos numeros:${mediaNum}`);
console.log(`maior numero:${maiorNum}`);
console.log(`menor numero:${menorNum}`);
console.log(`mediaPar:${mediaPar}`);
console.log(`pctimpar:${pctImpar.toPrecision(2)}`);
