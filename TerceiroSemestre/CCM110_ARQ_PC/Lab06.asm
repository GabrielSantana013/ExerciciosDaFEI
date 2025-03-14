;;2-)CRIE UM PROGRAMA QUE FIQUE ALTERNANDO
;;A ROTAÇÃO A ESQUERDA E A ROTAÇÃO A
;;DIREITA NA PORTA P1, FAÇA COM QUE ESSA
;;ROTAÇÃO SEJA ALTERNADA A CADA 1 VOLTA
;;COMPLETA

;MOV R0, #07
;MOV A, #11111110b
;MOV P1, A

;IDA:
;RL A
;MOV P1, A
;DJNZ R0, IDA

;MOV R0, #07
;VOLTA:
;RR A
;MOV P1, A
;DJNZ R0, VOLTA
;MOV R0, #07
;SJMP IDA

;;3-)Coloque cada dígito do seu número de matricula na memória iniciando 
;;no endereço 30h (cada número em 
;;um byte da memória).
;;;Escreva uma subrotina que contém 
;;um laço de repetição que copie os 
;;valores do vetor iniciando no 
;;endereço 30h para um outro vetor 
;;iniciando no endereço 40h.
;;Termine o programa com um laço 
;;infinito

;MAIN:
;MOV 30h, #02
;MOV 31h, #04
;MOV 32h, #01
;MOV 33h, #02
;MOV 34h, #04
;MOV 35h, #00
;MOV 36h, #07
;MOV 37h, #01
;MOV 38h, #02
;MOV R0, #30H
;MOV R1, #40H
;MOV R2, #09 
;LCALL COPIA

;COPIA:
;MOV A, @R0
;MOV @R1, A
;INC R1
;INC R0
;DJNZ R2, COPIA
;RET

;;4-)TESTE E VERIFIQUE O QUE FAZ ESSE 
;;PROGRAMA OBSERVE O VALOR DO SP E 
;;O QUE ESTA SENDO ARMAZENADO NA
;;PILHA

;;R:A CADA CHAMADA O SP APONTA PARA 
;;A PILHA, A PILHA COMECA A PARTIR DO
;;ENDERECO DE MEMORIA 8, E ANDA DE 2 EM
;;2 DE TRÁS PRA FRENTE. A CADA RET
;;O SP DECREMENTA E APONTA PARA A PRO
;;XIMA PILHA

;Principal:
;MOV A, #11h
;LCALL FUNC01
;SJMP $

;org 1100h
;FUNC01:
;MOV 30H, #33h
;LCALL FUNC02
;NOP
;RET

;org 2130h
;FUNC02:
;MOV 40H, #01H
;LCALL FUNC03
;NOP
;RET

;org 30A0h
;FUNC03:
;MOV 40H, #50H
;RET


;; 5-)Funções iterativas são funções 
;;que utilizam estruturas de 
;;controle de fluxo iterativas, 
;;como loops, para repetir uma 
;;sequência de instruções até que 
;;uma condição seja atendida.
;;Qual é a diferença entre uma função
;;recursiva e uma função 
;;iterativa em termos de desempenho e 
;;consumo de memória?

;;R: a função recursiva consome mais 
;;memória pois ela "chama" ela mesma,
;;fazendo com que armazenemos um endereço
;;de retorno a cada chamada

;;6-)Qual é o principal problema que
;;pode ocorrer quando criamos 
;;funções recursivas em programas? 
;;Como podemos evitá-lo?.

;R: loops infinitos, podemos 
;evita-los sempre impondo uma condicao
;de parada.

;;7-) Faça uma função recursiva 
;;(sub-rotina recursiva) com o 
;;problema que você respondeu no 
;;exercício anterior. Execute o 
;;programa e apresente a imagem 
;;da Tela do programa executado.

;PRINCIPAL:

;MOV A, #05
;MOV R0, A
;LCALL FUNC01

;FUNC01:
;MOV A, #06
;LCALL FUNC01
;RET


