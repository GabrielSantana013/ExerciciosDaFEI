#include <stdio.h>

void print_entrada(int *vetor, int tamanho){

    for(int i = 0; i < tamanho; i++){
        printf("%d ", vetor[i]);
    }
}

//porcaria O(n²)
void selection_sort(int* vetor, int tamanho){
    for(int i = 0; i < tamanho-2; i++){
        int min = i;
        for(int j = i+1; j < tamanho-1; j++){
            if(vetor[j] < vetor[min]){
                min = j;
            }
        }
        if(vetor[i] != vetor[min]){
            int temp = vetor[min];
            vetor[min] = vetor[i];
            vetor[i] = temp;
        }

    }
}


int main(){

    int entrada[] = {5,2,8,1,3,9};
    int tamanho = sizeof(entrada) / sizeof(entrada[0]);
    printf("\n Antes do Selection: ");
    print_entrada(entrada, tamanho);
    printf("\n Depois do Selection: ");
    selection_sort(entrada, tamanho);
    print_entrada(entrada, tamanho);

    return 0;
}