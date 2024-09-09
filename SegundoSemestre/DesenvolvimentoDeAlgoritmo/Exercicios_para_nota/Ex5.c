#include <stdio.h>

/*
Manipulação de Ponteiros em String: Implemente uma função que
recebe uma string como entrada e retorna a mesma string, mas com
todas as letras convertidas para maiúsculas. 
Use ponteiros para percorrer a string.
*/


void toUpper(char *ptrString)
{
    //como é string ele já sabe qnd é o final
    while(*ptrString)
    {
        if(*ptrString >= 97 || *ptrString >= 122)
        {
            *ptrString -= 32;
        }
        ptrString++;
    } 
}

int main(){

    char string [255];
    char *ptrString = &string[0];

    printf("Digite uma string: \n");
    fgets(string, sizeof(string), stdin);
    printf("String em Maiusculo: \n");
    toUpper(ptrString);
     while(*ptrString != '\0')
    {
        printf("%c", *ptrString);
        ptrString++;
    } 

    return 0;
}