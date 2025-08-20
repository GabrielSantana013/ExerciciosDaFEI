#include <stdio.h>
#include <stdlib.h>

typedef struct Celula{
    int valor;
    struct Celula *proximo;
}Celula;

typedef struct Pilha{
    Celula *topo;
    int qtt;
}Pilha;

Celula *criar_celula(int valor){
    Celula *nova_celula = malloc(sizeof(Celula));
    nova_celula->proximo = NULL;
    nova_celula->valor = valor;
    return nova_celula;
}

Pilha *criar_pilha(){
    Pilha *pilha = malloc(sizeof(pilha));
    pilha->qtt = 0;
    return pilha;
}


void push(int valor, Pilha *pilha){
    Celula *nova = criar_celula(valor);
    nova->proximo = pilha->topo;
    pilha->topo = nova; 
    pilha->qtt ++;
}

void imprime_pilha(Pilha *pilha){
    Celula *atual = pilha->topo;
    printf("TOPO -> ");
    while(atual != NULL){
        printf("%d ", atual->valor);
        atual = atual->proximo;
    }
    printf("<- BASE\n");
}

int pop(Pilha *pilha){
    if(pilha->qtt == 0){
        return -1;
    }
    int valor = pilha->topo->valor;
    Celula *tmp = pilha->topo;
    pilha->topo = pilha->topo->proximo;
    free(tmp);
    pilha->qtt--;
    return valor;
}


int main(){

    Pilha *p = criar_pilha();
    for(int i = 0; i < 10; i++){
        push(i,p);
        imprime_pilha(p);
    }

    for(int i = 0; i < 10; i++){
        printf("Valor do topo: %d\n", pop(p));
        imprime_pilha(p);
    }
    return 0;
}