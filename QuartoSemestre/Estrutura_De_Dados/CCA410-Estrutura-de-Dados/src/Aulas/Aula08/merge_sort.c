#include <stdio.h>
#include <stdlib.h>

void merge(int *vetor, int inicio, int meio, int fim){

    int n1 = meio - inicio + 1;
    int n2 = fim - meio;

    int *esquerda = malloc(n1 * sizeof(int));
    int *direita = malloc(n2 * sizeof(int));

    for(int  i = 0; i < n1; i++){
        esquerda[i] = vetor[inicio + i];
    }
    for(int j = 0; j < n2; j++){
        direita[j] = vetor[meio + 1 + j];
    }

    int i = 0, j = 0, k = inicio;
    while(i < n1 && j < n2){
        if(esquerda[i] <= direita[j]){
            vetor[k] = esquerda[i];
            i++;
        } else {
            vetor[k] = direita[j];
            j++;
        }
        k++;
    }

    // Copia os que sobraram na esquerda[]
    while(i < n1){
        vetor[k] = esquerda[i];
        i++;
        k++;
    }

    // Copia os que sobraram na direita[]
    while(j < n2){
        vetor[k] = direita[j];
        j++;
        k++;
    }

    free(esquerda);
    free(direita);
}

void merge_sort(int *vetor, int inicio, int fim){
    if(inicio < fim){
        int meio = (inicio + fim) / 2;
        merge_sort(vetor, inicio, meio);
        merge_sort(vetor, meio + 1, fim);
        merge(vetor, inicio, meio, fim);
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

    merge_sort(vetor, 0, tamanho - 1);

    printf("Vetor ordenado: ");
    print_array(vetor, tamanho);

    return 0;
}