/*Cadastro de Produtos usando Struct: Crie uma estrutura de dados chamada "Produto" que armazena nome, preço e quantidade em estoque.
Permita ao usuário cadastrar produtos, exibir as informações e calcular o valor total em estoque (preço * quantidade).*/

#include <stdio.h>


typedef struct Produto
{
    char nome[30];
    float preco;
    int qttEstoque;

} Produto;

void cadastrar(struct Produto *ptr)
{
    //limpa o buffer
    setbuf(stdin, NULL);
    printf("Digite o nome do produto: ");
    gets(ptr->nome);
    printf("Digite o preco do produto: ");
    scanf("%f", &ptr->preco);
    printf("Digite a quantidade do produto: ");
    scanf("%d", &ptr->qttEstoque);

}

void exibirItens(struct Produto *ptr){

    char buscaNome[30];
    printf("Digite o nome do produto para ver seus dados: ");

}

int main(void)
{

    Produto *ptr, produtos;
    ptr = &produtos;
    int menu;
    do
    {
        printf("\t1 - Cadastrar item\n");
        printf("\t2 - Exibir itens\n");
        printf("\t3 - Calcular valor total\n");
        printf("\t0 - Sair\n");
        scanf("%d", &menu);

        switch (menu)
        {
        case 1:
            cadastrar(ptr);
            break;
        case 2:
            exibirItens(ptr);
            break;
        case 0:
            exit(0);
            break;
        default:
            break;
        }
        
    }while (menu != 0);

    return 0;
}