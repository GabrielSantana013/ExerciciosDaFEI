#include <stdio.h>
#include <stdlib.h>

int partition(int *vetor, int inicio, int fim){
    int pivo = vetor[fim];
    int i = (inicio - 1);

    for(int j = inicio; j < fim; j++){
        if(vetor[j] <= pivo){
            i++;
            int temp = vetor[i];
            vetor[i] = vetor[j];
            vetor[j] = temp;
        }
    }
    int temp = vetor[i + 1];
    vetor[i + 1] = vetor[fim];
    vetor[fim] = temp;
    return i + 1;

}

void quick_sort(int *vetor, int inicio, int fim){
    if(inicio < fim){
        int meio = partition(vetor, inicio, fim);
        quick_sort(vetor, inicio, meio - 1);
        quick_sort(vetor, meio + 1, fim);
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

    quick_sort(vetor, 0, tamanho - 1);

    printf("Vetor ordenado: ");
    print_array(vetor, tamanho);

    return 0;
}