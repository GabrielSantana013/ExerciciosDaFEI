//Soma de Elementos em um Array: Crie um programa que solicita ao usuário inserir elementos em um array e calcule a soma desses elementos.

#include <stdio.h>

int main(){

    int numeros[11], resultado = 0;

    printf("Digite 10 numeros:\n");
    for(int i = 0; i < 10; i++)
    {
        scanf("%d", &numeros[i]);
    }

    for(int i = 0; i < 10; i++)
    {
        resultado += numeros[i];
    }
    printf("A soma dos numeros digitados e: %d", resultado);

    return 0;
}