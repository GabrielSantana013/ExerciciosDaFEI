/*
Cálculo de Estatísticas em um Array: Escreva um programa que
recebe um array de números e calcula a média,
mediana e moda dos elementos.
*/

#include <stdio.h>
#include <stdlib.h>

void media(int *vetor, int n)
{

    double media = 0;

    for (int i = 0; i < n; i++)
    {
        media += vetor[i];
    }
    printf("Media: %.2f\n", media / n);
}

void mediana(int *vetor, int n)
{

    if (n % 2 != 0)
    {
        printf("Mediana: %d\n", vetor[n / 2]);
    }
    else
    {
        printf("Mediana: %.2f\n", (vetor[n / 2] + vetor[n / 2 - 1]) / 2.0);
    }
}

void moda(int* vetor, int n) {

    int moda = 0;
    int cont = 0;
    int contModa = 0;

    for(int i = 0; i < n; i++)
    {
        for(int j = 0; j < n; j++)
        {
            if(vetor[i] == vetor[j])
            {
                cont++;
            }
        }
        if(cont > contModa)
        {
            moda = vetor[i];
            contModa = cont;
        }
        cont = 0;
    }

    if (contModa == 1) {
        printf("Não existe moda\n");
    } else {
        printf("Moda: %d\n", moda);
    }
}

int main()
{

    int n;
    printf("Digite o tamanho do array: ");
    scanf("%d", &n);

    int *vetor = malloc(n * sizeof(int));

    for (int i = 0; i < n; i++)
    {
        printf("Digite o valor da posicao %d: ", i);
        scanf("%d", &vetor[i]);
    }

    media(vetor, n);
    mediana(vetor, n);
    moda(vetor, n);


    return 0;
}