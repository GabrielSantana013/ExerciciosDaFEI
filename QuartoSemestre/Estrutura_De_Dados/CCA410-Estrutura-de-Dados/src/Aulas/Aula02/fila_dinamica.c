#include <stdio.h>
#include <stdlib.h>

typedef struct Celula{
    int value;
    Celula *next;
    Celula *previous;

}Celula;

typedef struct Fila{
    int qtt;
    Celula *head;
    Celula *tail;
}Fila;

Fila *criar_fila(){
    Fila *fila = malloc(sizeof(fila));
    fila->qtt = 0;
    fila->previous = NULL;
    fila->next = NULL;
    return fila;
}

Celula *criar_celula(int valor){
    Celula *celula = malloc(sizeof(celula));
    celula->valor = valor;
    celula->next = NULL;
    celula->previous = NULL;
    return celula;
}

void enqueue(Fila *fila, Celula *celula){
    if(fila->qtt == 0){
        fila->head = celula;
        fila->tail = celula->next;
        fila->qtt++;
    }
    fila->head = 
}

void dequeue(){

}

void imprime_fila(){

}

int main(){

    return 0;
}