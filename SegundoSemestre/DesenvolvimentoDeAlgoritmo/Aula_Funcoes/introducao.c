#include <stdio.h>
#include "soma.h"


int main(void){

    int numero;

    scanf("%d",&numero);
    printf("O numero digitado e: %d\n", numero);
    printf("Hello world \n");
    float c = soma(5.4,3.2);
    printf("%.2f", c);
    return 0;
}