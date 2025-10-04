#include <stdio.h>
#include <stdlib.h>

void max_heapify(int *vetor, int tamanho, int i){
    int esquerda = 2 * i + 1;
    int direita = 2 * i + 2;
    int maior = i;

    if(esquerda < tamanho && vetor[esquerda] > vetor[maior]){
        maior = esquerda;
    }
    if(direita < tamanho && vetor[direita] > vetor[maior]){
        maior = direita;
    }
    if(maior != i){
        int temp = vetor[i];
        vetor[i] = vetor[maior];
        vetor[maior] = temp;
        max_heapify(vetor, tamanho, maior);
    }
}

void build_max_heap(int *vetor, int tamanho){
    for(int i = tamanho / 2 - 1; i >= 0; i--){
        max_heapify(vetor, tamanho, i);
    }
}

void heap_sort(int *vetor, int tamanho){
    build_max_heap(vetor, tamanho);
    for(int i = tamanho - 1; i > 0; i--){
        int temp = vetor[0];
        vetor[0] = vetor[i];
        vetor[i] = temp;
        max_heapify(vetor, i, 0);
    }
}



void print_array(int *vetor, int tamanho){
    for(int i = 0; i < tamanho; i++){
        printf("%d ", vetor[i]);
    }
    printf("\n");
}


int main(){

    int vetor[] = {8, 2, 1, 6, 7, 0, 3, 5, 4, 9};
    int tamanho = sizeof(vetor) / sizeof(vetor[0]);

    printf("Vetor original: ");
    print_array(vetor, tamanho);
    printf("Vetor ordenado: ");
    heap_sort(vetor, tamanho);
    print_array(vetor, tamanho);

    return 0;
}