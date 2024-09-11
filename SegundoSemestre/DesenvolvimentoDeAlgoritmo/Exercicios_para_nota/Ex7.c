/*
Ordenação de Structs: Crie um programa que ordena um array de structs com base em um dos campos (por exemplo, idade) 
usando qsort da biblioteca glibc.
*/

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

typedef struct Pessoa{

    char nome[255];
    int idade;
    float altura;

}Pessoa;


//O tipo do ponteiro é void para que a função possa ser usada em qualquer tipo de dado
int comparaNome(const void *a, const void *b)
{
    //antes de fazer a comparação, é necessário fazer um cast para o tipo de dado que será comparado
    //nesse caso, se o strcmp retornar um valor maior que 1, a string a é maior que a string b
    //se o strcmp retornar um valor menor que 1, a string a é menor que a string b
    //se o strcmp retornar 0, as strings são iguais
    return strcmp(((Pessoa*)a)->nome, ((Pessoa*)b)->nome);
}

int comparaIdade(const void *a, const void *b)
{
    //a mesma lógica do strcmp se aplica aqui
    return ((Pessoa*)a)->idade - ((Pessoa*)b)->idade;
}

int comparaAltura(const void *a, const void *b)
{
    return ((Pessoa*)a)->altura - ((Pessoa*)b)->altura;
}


int main(){

    int qttPessoas;
    int menu;
    printf("Digite a quantidade de pessoas que deseja cadastrar: ");
    scanf("%d", &qttPessoas);

    Pessoa *vetor = (Pessoa*) malloc(qttPessoas * sizeof(Pessoa));

    for(int i = 0; i < qttPessoas; i++)
    {
        printf("Digite o nome da pessoa %d: ", i+1);
        scanf("%s", vetor[i].nome);
        printf("Digite a idade da pessoa %d: ", i+1);
        scanf("%d", &vetor[i].idade);
        printf("Digite a altura da pessoa %d: ", i+1);
        scanf("%f", &vetor[i].altura);
    }

    printf("Digite o campo que deseja ordenar (crescente): ");
    printf("\t1 - Nome\n");
    printf("\t2 - Idade\n");
    printf("\t3 - Altura\n");
    scanf("%d", &menu);

    if(menu == 1)
    {
        qsort(vetor, qttPessoas, sizeof(Pessoa), comparaNome);
    }
    else if(menu == 2)
    {
        qsort(vetor, qttPessoas, sizeof(Pessoa), comparaIdade);
    }
    else if(menu == 3)
    {
        qsort(vetor, qttPessoas, sizeof(Pessoa), comparaAltura);
    }
    else
    {
        printf("Opcao invalida\n");
    }

    for(int i = 0; i < qttPessoas; i++)
    {
        printf("Nome: %s\n", vetor[i].nome);
        printf("Idade: %d\n", vetor[i].idade);
        printf("Altura: %.2f\n\n", vetor[i].altura);
    }

    return 0;
}