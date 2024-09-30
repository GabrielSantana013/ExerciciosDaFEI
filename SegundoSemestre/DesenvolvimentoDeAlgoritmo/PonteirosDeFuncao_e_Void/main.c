#include <stdio.h>

int soma(int a, int b)
{
    return a+b;
}

int subtracao(int a, int b)
{
    return a-b;
}

int (*ptrFuncao)(int,int) = soma;

int (*ptrFuncoes[])(int,int) = {soma, subtracao};

int main(){

printf("Soma com ptr de funcao: %d\n", ptrFuncao(5,5));
printf("Soma com vetor de funcoes (ptr):%d \n", ptrFuncoes[0](3,3));
printf("Subtracao com vetor de funcoes (ptr):%d \n", ptrFuncoes[1](5,2));
}

