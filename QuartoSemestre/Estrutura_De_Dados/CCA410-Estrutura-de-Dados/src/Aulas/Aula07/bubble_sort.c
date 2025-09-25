#include <stdio.h>

void print_entrada(int *vetor, int tamanho){

    for(int i = 0; i < tamanho; i++){
        printf("%d ", vetor[i]);
    }
}

//porcaria O(n²)
void bubble_sort(int* vetor, int tamanho){
    for(int i = 0; i < tamanho-1; i++){
        for(int j = 0; j < tamanho-1; j++){
            if(vetor[j] > vetor[j+1]){
                int temp = vetor[j];
                vetor[j] = vetor[j+1];
                vetor[j+1] = temp;
            }
        }
    }
}

int main(){

    int entrada[] = {5,4,8,10,1};
    int tamanho = sizeof(entrada) / sizeof(entrada[0]);

    printf("\n Antes do Bubble: ");
    print_entrada(entrada, tamanho);
    bubble_sort(entrada, tamanho);
    printf("\n Depois do Bubble: ");
    print_entrada(entrada, tamanho);
    return 0;
}