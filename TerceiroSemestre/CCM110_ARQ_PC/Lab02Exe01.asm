;PROGRAMA JOGA OS BITS À DIREITA

;MOV A, #0FEh
;ROT: 
;	RR A
;	MOV P1, A
;	AJMP ROT

;PROGRAMA USA SJMP (GOTO)
;MOV R1, #0FFh
;DEC R1
;SJMP TESTE
;EX01:
;	DEC R1
;	MOV A, R1
;	DEC A
;	SJMP FIM
;TESTE:
;	INC R1
;	SJMP EX01
;	DEC R1
;	MOV A,R1
;FIM:
;	MOV R2, A


;PROGRAMA JOGA OS BITS À ESQUERDA

;MOV A, #0FEH
;ROT:
;	RL A
;	MOV P1, A
;	AJMP ROT

;Zera p1.0 e p1.1 e incrementa, somando os bits
;CLR P1.0
;CLR P1.1
;LB:
;	INC P1
;	SJMP LB 
