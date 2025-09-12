#include <stdio.h>
#include <stdlib.h>

#define LEN 10 

typedef struct {
	int valores[LEN];
	int qtde;
} heap;

void swap(int *a, int *b){
    int temp = *a;
    *a = *b;
    *b = temp;
}


int filho_esq(int pai){
	return 2*pai+1;
}

int filho_dir(int pai){
	return 2*pai+2;
}

int pai(int filho){
	return (filho-1)/2;
}

int ultimo_pai(heap *h){
	return (h->qtde/2)-1;
}


void peneirar(heap *h, int pai){
	
    int esq = filho_esq(pai);
    int dir = filho_dir(pai);
    int maior;

    if(esq < h->qtde && h->valores[esq] > h->valores[pai]){
        maior = esq;
    }else{
        maior = pai;
    }
    if(dir < h->qtde && h->valores[dir] > h->valores[maior]){
        maior = dir;
    }

    if(pai != maior){
        swap(&h->valores[pai], &h->valores[maior] );
        peneirar(h, maior);
    }

}

void peneirar_para_cima(heap *h, int filho_idx){
	
    if(filho_idx <=0){ return;}

    int pai_idx = (filho_idx-1)/2;

    if(h->valores[pai_idx] < h->valores[filho_idx]){
        swap(&h->valores[pai_idx], &h->valores[filho_idx]);
        peneirar_para_cima(h, pai_idx);
    }

}


void construir(heap *h){
	for(int i = h->valores[ultimo_pai(h)]; i>=0; i--){
        peneirar(h, i);
    }
}

void inserir(heap *h, int valor){
	
    if(h->qtde >= LEN){
        return;
    }

    h->valores[h->qtde] = valor;
    peneirar_para_cima(h, h->qtde);
    h->qtde ++;

}

void remover(heap *h){
	if(h->qtde > 0){
        swap(&h->valores[0], &h->valores[h->qtde-1]);
        h->qtde --;
        if(h->qtde > 0){
            peneirar(h,0);
        }
    }
}


void mostrar(heap *h){
	for(int i = 0; i < h->qtde; i++){
        printf("%d ", h->valores[i]);
    }
    printf("\n");
}



int main(void) {
	heap *h = malloc(sizeof(heap));
	h->qtde = 0;
	
	
	// TESTE 1: Inserção e visualização
	printf("--- TESTE 1: Inserção de elementos ---\n");
	
	for(int i = 1; i <= 10; i++){
		inserir(h, i);
		printf("Inserido %d: ", i);
		mostrar(h);
	}
	
	
	// TESTE 2: Remoção sucessiva
	printf("\n--- TESTE 2: Remoção de elementos ---\n");
	printf("Removendo em ordem de prioridade:\n");
	
	while(h->qtde > 0) {
		int max = h->valores[0];
		printf("Removendo máximo %d: ", max);
		remover(h);
		mostrar(h);
	}
	

	free(h);	
	return 0;
}