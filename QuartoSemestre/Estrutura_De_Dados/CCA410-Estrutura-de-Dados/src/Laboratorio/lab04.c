#include <stdio.h>
#include <stdlib.h>

#define tam_hash 11

typedef struct Celula{
  int valor;
  struct Celula* proximo;
}Celula;

typedef struct {
  Celula* inicio;
}Lista;

typedef struct {
  Lista* table[tam_hash];
}Hash;

Hash* start_hash(){
    Hash *h = (Hash*) malloc(sizeof(Hash));
    //se a alocação falhar, retorna nulo
    if(h == NULL){
        return NULL;
    }

    //inicializa cada posição do vetor como uma lista
    for(int i = 0; i < tam_hash; i++){
        h->table[i] = (Lista*) malloc(sizeof(Lista));
        //se falhar, retorna nulo
        if(h->table[i] == NULL){return NULL;}
        h->table[i]->inicio = NULL;
    }
    return h;
}

void inserir_hash(Hash* hash, int valor){
  //pega o indice usando kmod(m)  
  int indice = (valor%tam_hash);

  //cria uma tabela que recebe a tabela do índice no hash
  Lista *lista = hash->table[indice];

  //cria uma nova célula
  Celula *nova = (Celula*) malloc(sizeof(Celula));
  nova->valor = valor;
  nova->proximo = NULL;

  //significa que a lista ta vazia na primeira posição
  if(lista->inicio == NULL){
    lista->inicio = nova;
    return;
  }

  nova->proximo = lista->inicio;
  lista->inicio = nova;

}

void remover_hash(Hash* hash, int valor){
  
    int indice = valor%tam_hash;
    Lista *lista = hash->table[indice];

    Celula *atual = lista->inicio;
    Celula *anterior = NULL;

    //não achou logo de cara
    while(atual != NULL){
    if(atual->valor == valor){
        //sempre vai ser null pq o anterior é inicializado como null
        if(anterior == NULL){
            lista->inicio = atual->proximo;
        }else{
            anterior->proximo = atual->proximo;
        }
            free(atual);
            return;
        }
        anterior = atual;
        atual = atual->proximo;
    }
}

void imprimir(Hash* hash) {
    printf("---------------------\n");
    for (int i = 0; i < tam_hash; i++) {
        printf("%d ->", i);
        Celula* atual = hash->table[i]->inicio;
        while (atual != NULL) {
            printf(" %d", atual->valor);
            atual = atual->proximo;
        }
        printf(" \n");
    }
    printf("---------------------\n");
}


int main(void) {
  Hash* hash = start_hash();
  int valor;
  while(1){
    scanf("%d", &valor);
    if(valor == 0)
      break;
    inserir_hash(hash, valor);
  }
  imprimir(hash);
  while(1){
    scanf("%d", &valor);
    if(valor == 0)
      break;
    remover_hash(hash, valor);
  }
  imprimir(hash);
  return 0;
}