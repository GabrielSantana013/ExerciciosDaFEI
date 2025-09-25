#include <stdio.h>

void print_entrada(int *vetor, int tamanho){

    for(int i = 0; i < tamanho; i++){
        printf("%d ", vetor[i]);
    }
}

//Porcaria O(n²)
void insertion_sort(int* vetor, int tamanho){
    for(int j = 1; j < tamanho-1; j++){
        int chave = vetor[j];
        int i = j-1;
        while(i >=0 && vetor[i] > chave){
            vetor[i+1] = vetor[i];
            i--;
        }
        vetor[i+1] = chave;
    }
}


int main(){

    int entrada[] = {5,2,8,1,3,9};
    int tamanho = sizeof(entrada) / sizeof(entrada[0]);
    printf("\n Antes do Insertion: ");
    print_entrada(entrada, tamanho);
    printf("\n Depois do Insertion: ");
    insertion_sort(entrada, tamanho);
    print_entrada(entrada, tamanho);

    return 0;
}