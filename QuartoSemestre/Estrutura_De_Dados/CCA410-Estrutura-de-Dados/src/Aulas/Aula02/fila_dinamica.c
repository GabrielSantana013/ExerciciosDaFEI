#include <stdio.h>
#include <stdlib.h>

typedef struct Celula{
    int value;
    struct Celula *next;
    struct Celula *previous;

}Celula;

typedef struct Fila{
    int qtt;
    Celula *head;
    Celula *tail;
}Fila;

Fila *criar_fila(){
    Fila *fila = malloc(sizeof(Fila));
    fila->qtt = 0;
    fila->head = NULL;
    fila->tail = NULL;
    return fila;
}

Celula *criar_celula(int valor){
    Celula *celula = malloc(sizeof(Celula));
    celula->value = valor;
    celula->next = NULL;
    celula->previous = NULL;
    return celula;
}

void enqueue(Fila *fila, int valor){

    Celula *novo = criar_celula(valor);

    //primeira inserção na fila
    if(fila->head == NULL){
        fila->head = novo;
        fila->tail = novo;
        //inserção no final da fila
    }else{
        fila->tail->next = novo;
        novo->previous = fila->tail;
        fila->tail = novo;
    }
    fila->qtt++;
}

void dequeue(Fila *fila){
    if(fila->qtt == 0){
        fila->head = NULL;
        fila->tail = NULL;
        return;
    }
    Celula *temp = fila->head;
    fila->head = temp->next;
    free(temp);
    fila->qtt--;
}

void imprime_fila(Fila *fila){

    Celula *cel = fila->head;

    printf("Comeco -> ");
    while(cel != NULL){
        printf("%d", cel->value);
        cel = cel->next;
    }
    printf(" <-Final\n");
}

int main(){

    Fila *fila = criar_fila();
    for(int i = 0; i < 10; i++){
        enqueue(fila, i);
        imprime_fila(fila);
    }
    for(int i = 0; i < 10; i++){
        dequeue(fila);
        imprime_fila(fila);
    }
    return 0;
}