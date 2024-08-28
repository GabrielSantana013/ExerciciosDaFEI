/*Cadastro de Produtos usando Struct: Crie uma estrutura de dados chamada "Produto" que armazena nome, preço e quantidade em estoque.
Permita ao usuário cadastrar produtos, exibir as informações e calcular o valor total em estoque (preço * quantidade).*/

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct Produto
{
    char nome[30];
    float preco;
    int qttEstoque;

} Produto;


int cadastrar(struct Produto *ptr)
{
    int n;
    printf("Digite a quantidade de produtos a serem cadastrados: ");
    scanf("%d", &n);

    for (int i = 0; i < n; i++)
    {
        // limpa o buffer
        setbuf(stdin, NULL);
        printf("Digite o nome do produto: ");
        fgets(ptr->nome, sizeof(ptr->nome), stdin);
        printf("Digite o preco do produto: ");
        scanf("%f", &ptr->preco);
        printf("Digite a quantidade do produto: ");
        scanf("%d", &ptr->qttEstoque);
        ptr++;
    }
    return n;
}

void exibirItens(struct Produto *ptr){

    char nome[30];
    int achou = 1;
    printf("\nDigite o nome do produto para ver seus dados: ");
    //limpa buffer
    setbuf(stdin, NULL);
    fgets(nome, sizeof(nome), stdin);

    for(int i = 0; i < 20; i++)
    {
        if(strcmp(nome, ptr->nome) == 0)
        {
            printf("\nNome: %s", ptr->nome);
            printf("Preco: %.2f\n", ptr->preco);
            printf("Quantidade em estoque: %d\n\n", ptr->qttEstoque);
            achou--;
        }
        ptr++;
    }
    if(achou)
    {
        printf("\nProduto nao encontrado\n\n");
    }
}

void calcularValorTotal(struct Produto *ptr, int produtosCadastrados)
{
    float total = 0.0;
    for (int i = 0; i < produtosCadastrados; i++)
    {
        total += ptr->preco * ptr->qttEstoque;
        ptr++;
    }
    printf("Valor total em estoque: %.2f\n", total);
}

int main(void)
{

    Produto *ptr, produtos[20];
    ptr = &produtos[0];
    int menu;
    int produtosCadastrados = 0;
    do
    {
        printf("\tMaximo 20 itens\n");
        printf("\t1 - Cadastrar item\n");
        printf("\t2 - Exibir itens\n");
        printf("\t3 - Calcular valor total\n");
        printf("\t0 - Sair\n");
        scanf("%d", &menu);

        switch (menu)
        {
        case 1:
            produtosCadastrados+= cadastrar(ptr);
            break;
        case 2:
            exibirItens(ptr);
            break;
        case 3:
            calcularValorTotal(ptr, produtosCadastrados);
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