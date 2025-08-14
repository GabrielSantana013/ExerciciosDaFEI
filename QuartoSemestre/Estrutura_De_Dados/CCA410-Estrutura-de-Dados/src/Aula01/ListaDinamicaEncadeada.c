#include <stdio.h>
#include <stdlib.h>

typedef struct Cel{
    int value;
    struct Cel *ptrNextCel;
}Cel;

typedef struct LDE{
    int elementsNumber;
    Cel *firstElement;
}LDE;

Cel *create_cel(int value){
    Cel *newCel = malloc(sizeof(Cel));
    newCel->value = value;
    newCel->ptrNextCel = NULL;
    return newCel;
}

LDE *create_list(){
    LDE *newList = malloc(sizeof(LDE));
    newList->elementsNumber = 0;
    newList->firstElement = NULL;
    return newList;
}

void insert(LDE *list, int value){
    Cel *newCel = create_cel(value);
    Cel *anterior = NULL;
    Cel *atual = list->firstElement;
    while(atual != NULL && atual->value < value){
        anterior = atual;
        atual = atual->ptrNextCel;
    }
    if(anterior == NULL){
        newCel->ptrNextCel = list->firstElement;
        list->firstElement = newCel;
    }else{
        anterior->ptrNextCel = newCel;
        newCel->ptrNextCel = atual;
    }
    list->elementsNumber++;
}

void removeCel(LDE *list, int value){
    Cel *atual = list->firstElement;
    Cel *anterior = NULL;

    while(atual != NULL && atual->value != value){
        anterior = atual;
        atual = atual->ptrNextCel;
    }
    //andou a lista toda e não encontrou o value
    if(atual == NULL){
        printf("Não encontrei o target");
        return;
    }
    //quer remover o primeiro da lista
    if(anterior == NULL){
        printf("remover o primeiro da lista");
        list->firstElement = atual->ptrNextCel;
    //achou o value    
    }else{
        printf("achei o target");
        anterior->ptrNextCel = atual->ptrNextCel;
    }
    free(atual);
    list->elementsNumber--;
}

void printList(LDE *list){
    Cel *atual = list->firstElement;
    while(atual != NULL){
        printf("%d ", atual->value);
        atual = atual->ptrNextCel;

    }
    printf("\n");
}

int main(){

    LDE *list = create_list();
    
    for(int i = 2; i >= 0; i--){
        insert(list, i);
        printList(list);

    }
    removeCel(list, 0);
    printList(list);
    return 0;
}
