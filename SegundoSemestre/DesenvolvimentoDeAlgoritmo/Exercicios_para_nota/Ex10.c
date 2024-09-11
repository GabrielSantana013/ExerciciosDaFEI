/*
Manipulação de Tempo: Utilize a biblioteca time.h para calcular o tempo que 
um determinado trecho de código leva para ser executado.
*/

#include <stdio.h>
#include <time.h>

void buscaNormal(unsigned long int n){

    int encontrado = 0;

    for(unsigned long int i = 0; i < 1000000000; i++)
    {
        if(i == n){
            printf("Numero encontrado: %ld\n", i);
            encontrado = 1;
            break;
        }
    }
    if(!encontrado)
    {
        printf("Numero nao encontrado\n");
    }

}

void buscaBinaria(unsigned long int n){

    unsigned long int encontrado = 0;
    unsigned long int inicio = 0;
    unsigned long int fim = 999999999;
    unsigned long int meio;

    while(inicio <= fim)
    {
        meio = (inicio + fim) / 2;
        if(meio == n){
            printf("Numero encontrado: %ld\n", meio);
            encontrado = 1;
            break;
        }
        else if(meio < n){
            inicio = meio + 1;
        }
        else{
            fim = meio - 1;
        }
    }
    if(!encontrado)
    {
        printf("Numero nao encontrado\n");
    }
}


int main(){

    //variavel do tipo clock para armazenar o numero de clocks que é retornado de clock()
    clock_t start;
    double tempoTotal = 0;

    unsigned long int n;
    printf("Digite um numero entre 0 e 1.000.000.000: ");
    scanf("%ld", &n);

    start = clock();
    buscaNormal(n);

    //calculo do tempo de execução (numero de clocks/clocks por segundo) = tempo de execução em segundos
    tempoTotal = (double)(clock() - start) / CLOCKS_PER_SEC;    
    printf("Tempo de execucao da busca normal: %.6f\n", tempoTotal);

    start = clock();
    buscaBinaria(n);

    tempoTotal = (double)(clock() - start) / CLOCKS_PER_SEC;
    printf("Tempo de execucao da busca binaria: %.6f\n", tempoTotal);



    return 0;
}