Exercício 1:

Calcule quanto tempo será gasto por esta subrotina, 
considerando um cristal de 12MHz?

```asm
org 080h
ZERAR:
CLR A  			    // 1uS
MOV R0, #99 		// 1uS
ROT:
MOV @R0, A 		  // 1uS
NOP			        // 1uS
DJNZ R0, ROT		// 2uS
RET			        // 2uS
```
2uS + 396uS + 2uS = 400uS

Exercício 2: 

Os 3 programas a seguir apresenta três possíveis soluções para o problema de se zerarem os endereços de memória 30h até 38h. 

Compare as soluções levando em conta:

➢ o tamanho do programa e;

➢ o tempo de execução.

sol 1: 27 bytes e 18uS.

sol 2: 8 bytes e 38uS. 

sol 3: 19 bytes e 10uS. 


Exercício 3:

Escreva no site replit em Linguagem C o programa dado abaixo, porém 
coloque na variável valor do tipo int os 8 primeiros dígitos do seu número de 
matrícula. Para entrega apresente a imagem da tela com o resultado da 
execução desse programa. 
O computador armazenou como Big-endian ou Little-endian ?

R: O computador armazenou do bit menos significativo para o mais significativo, ou seja, Little-endian.


Exercício 4:
Qual é a diferença entre tempo de ciclo de máquina e clock da 
frequência da máquina em arquitetura de computadores?

r: O ciclo de máquina é o número de ciclos de clock (oscilações) necessários para executar uma instrução (isso depende da instrução e varia de processador para processador).
Já o clock da frequência é quantas vezes ele oscila por segundo, variando de processador para processador.

Como a melhoria do tempo de ciclo de uma CPU pode melhorar 
o desempenho geral de um computador?

r: Se melhorarmos o tempo de ciclo de uma CPU, seremos capazes de realizar mais instruções por segundo.


Exercício 5:

Escreva uma subrotina que consuma exatamente 8ms (ou 
seja, 8000us), considerando que se usa um cristal de 12 MHz.


```asm
DELAY:
MOV R0, #63 ; 1uS

ROT1:
MOV R1, #61 ; 1uS
ROT2:

DJNZ R1, ROT2 ;2uS
DJNZ R0, ROT1 ;2uS 

; falta 127uS (7869)

MOV R2, #64
ROT3:
DJNZ R2, ROT3
```


