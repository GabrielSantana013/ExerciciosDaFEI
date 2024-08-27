//Manipulação de Strings: Desenvolva um programa que recebe uma string do usuário e conta o número de vogais nela.

#include <stdio.h>

int main(void){

    char entrada[30];
    int vogais = 0;
    printf("Digite uma string para saber o numero de vogais: \n");
    gets(entrada);

    for(int i = 0; entrada[i] != '\0'; i++)
    {
        if(entrada[i] == 'a' || entrada[i] == 'A' ||
           entrada[i] == 'e' || entrada[i] == 'E' ||
           entrada[i] == 'i' || entrada[i] == 'I' ||
           entrada[i] == 'o' || entrada[i] == 'O' ||
           entrada[i] == 'u' || entrada[i] == 'U')
        {
            vogais++;
        }
    }

    printf("A quantidade de vogais na string e: %d", vogais);

    return 0;
}