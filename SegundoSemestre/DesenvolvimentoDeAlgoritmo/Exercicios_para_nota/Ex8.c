/*
Manipulação de Ponteiros: Implemente uma função que recebe um array
e seu tamanho como argumentos e retorna um novo array invertido,
utilizando ponteiros.
*/

#include <stdio.h>
#include <stdlib.h>

int* inverter(int* vetor, int n){

    int *ptrInicio = vetor;
    int *ptrFim = vetor + n - 1;

    int *vetorInvertido = malloc(n*sizeof(int));
    
    while(ptrInicio <= ptrFim)
    {
        *vetorInvertido = *ptrFim;
        vetorInvertido++;
        ptrFim--;
    }
    vetorInvertido -= n; //voltando o ponteiro para a primeira posição do vetor invertido

    return vetorInvertido;
}


int main()
{
    int n;
    printf("Digite o tamanho do array: ");
    scanf("%d", &n);

    int* vetor = malloc(n* sizeof(int));

    for(int i = 0; i < n; i++)
    {
        printf("Digite o valor da posicao %d: ", i);
        scanf("%d", &vetor[i]);
    }

    printf("Vetor original: \n");

    for(int i = 0; i < n; i++)
    {
        printf("%d ", vetor[i]);
    }
    printf("\n");

    vetor = inverter(vetor, n);

    printf("Vetor invertido: \n");
    for(int i = 0; i < n; i++)
    {
        printf("%d ", vetor[i]);
    }

    return 0;
}