;MOV A, #10H
;MOV R0, #20H
;MOV R1, #20H
;LCALL SOMA
;MOV R0, #50H
;MOV R1, #50H
;LCALL SOMA
;SJMP $


;SUBROTINA DE SOMA R2 = R1+R0
;SOMA:
;MOV A, R0
;ADD A, R1
;MOV R2, A
;RET

;O REGISTRADOR PC (PROGRAM COUNTER)
;MARCA A INSTRUÇÃO A SER EXECUTADA

;O REGISTRADOR SP (STACK POINTER)
;APONTA PARA O ENDEREÇO DA PILHA


;org 0000h
;LJMP START ;Pula incondicionalmente para START
;org 0003h
;INT_EXT0: 
;CPL P1.0 ;complementa P1.0
;RETI ;Retorna da interrupção
;org 0080h
;START: 
;SETB EA ;Habilita as interrupções
;SETB EX0 ;Habilita a interrupção 0
;SETB IT0 ;Trabalhando com borda de descida
;SJMP $ ;Laço de repetição


NOP
NOP
MOV R0, #5
LOOP:
NOP
MOV A, #1
DJNZ R0, LOOP
NOP
NOP