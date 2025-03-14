;MOV A, #1

;;JZ DESVIA SE O ACUMULADOR FOR 0
;;JNZ DESVIA SE O ACUMULADOR NÃO FOR 0

;JZ DESVIO
;MOV A, #0
;SJMP FIM

;DESVIO:
;MOV A, #1
;FIM: 

;==============================

;;CJNE COMPARA E DESVIA SE N FOR IGUAL

;;CJNE OPERANDO1, OPERANDO2, ENDERECO

;MOV A, #11h

;CJNE A, #33h, ELSE
;MOV R1,A
;SJMP FIM

;ELSE:
;MOV R1,#2
;FIM:

;==============================

;;JB SALTA SE O BIT ESTIVER SETADO
;;JNB SALTA SE O BIT N ESTIVER SETADO

;VOLTA:
;JNB P2.1, ACENDE
;JNB P2.2, APAGA
;JB P2.1, ACENDE

;ACENDE: 
;CLR P1.0
;SJMP VOLTA

;APAGA: SETB P1.0
;SJMP VOLTA
;==============================

;;Qual o valor do bit “20h.0”
;;após:

;SETB C
;JC DESVIO
;CPL C
;MOV 20H.0, C

;DESVIO:
;CPL C
;MOV 20H.0, C

;R: 0
;==============================

;; Qual o valor final 
;;de R1 após o seguinte 
;;programa:

;R: 1

;MOV R0, #07H
;MOV R1, #00H
;DJNZ R0, CONTA
;SJMP SAIDA

;CONTA:
;INC R1

;SAIDA:
;NOP

;==============================

;; QUAL O VALOR FINAL DE R1 APÓS
;;O SEGUINTE PROGRAMA:

;;R: 7

;MOV R0, #07H
;MOV R1, #00H

;CONTA:
;INC R1
;DJNZ R0, CONTA

;SAIDA:
;NOP

;==============================
;; CRIE UM PROGRAMA QUE ESCREVA 1
;; EM TODAS AS POSICOES DA RAM INTERNA
;; OU SEJA, DO ENDERECO 0 ATE O ENDERECO 127
;; DA RAM INTERNA

;MOV R0, #127
;LOOP:
;MOV @R0, #0
;DJNZ R0, LOOP

;NOP
;NOP
;==============================

;;CONSTRUIR E TESTAR UM PROGRAMA
;; QUE DEVE ALOCAR O VALOR EEH
;; EM 50 BYTES CONSECUTIVOS DA RAM
;;INTERNA INICIANDO NO ENDERECO 20H

;MOV R0, #20H
;MOV R1, #50h
;LOOP:
;MOV @R0, #0EEH
;INC R0
;DJNZ R1, LOOP
;NOP
;NOP

;==============================

;;COMPARE DOIS NUMEROS INTEIROS SEM SINAL
;;QUE ESTÃO LOCALIZADOS EM R7 E R6
;;ARMAZENE O MAIOR EM R7 E O MENOR
;;EM R6. TERMINE O PROGRAMA COM UM
;;LAÇO INFINITO

;MOV R7, #5
;MOV R6, #10

;COMP:
;MOV A, R7
;CLR C
;SUBB A,R6 ;;O SUB MODIFICA O CARRY

;JNC ROT1
;XCH A, R7 ;;TROCA OS NUMS
;XCH A, R6
;XCH A, R7
;ROT1:
;SJMP $