/*
Leitura e Escrita de Registros em Arquivos Binários: 
Desenvolva um programa que cria e manipula um arquivo binário para armazenar registros de funcionários. 
Cada registro deve conter nome, idade e salário. Permita ao usuário adicionar novos registros, 
listar todos os registros e buscar por registros específicos pelo nome.
*/

#include <stdio.h>

typedef struct Funcionario{

    char nome[255];
    int idade;
    float salario;

}Funcionario;

int adicionarRegistros(char* nome_arq, Funcionario *ptrFuncionario){

    int bytes = sizeof(*ptrFuncionario);

    //limpa buffer;
    fflush(stdin);
    printf("Digite o nome do funcionario: \n");
    fgets(ptrFuncionario->nome, bytes, stdin);
    //limpa buffer;
    fflush(stdin);
    printf("Digite a idade do funcionario: \n");
    scanf("%d", &ptrFuncionario->idade);
    printf("Digite o salario do funcionario: \n");
    scanf("%f", &ptrFuncionario->salario);

    FILE *pFile;
    pFile = fopen(nome_arq, "ab");

    if(pFile == NULL)
    {
        printf("Ocorreu um erro ao abrir o arquivo.");
        return 1;
    }
    
    fwrite(ptrFuncionario, bytes, 1, pFile);

    fclose(pFile);

    return 0;
}

int listarRegistros(char* nome_arq, Funcionario *ptrFuncionario){
    FILE *pFile = fopen(nome_arq, "rb");
    int bytes = sizeof(*ptrFuncionario);
    char linha[255];

    while(!feof(pFile))
    {
        fgets(linha, sizeof(linha), pFile);
        printf("%s", linha);
        fgets(linha, sizeof(linha), pFile);
        printf("%s", linha);
        fgets(linha, sizeof(linha), pFile);
        printf("%s", linha);
        printf("\n");
    }

    // while(fread(ptrFuncionario, bytes, 1, pFile) == 1)
    // {
    //     printf("Nome do funcionario: %s", ptrFuncionario->nome);
    //     printf("Idade do funcionario: %d\n", ptrFuncionario->idade);
    //     printf("Salario do funcionario: %.3f\n", ptrFuncionario->salario);
    //     printf("\n"); 
    // }

    return 0;
}

int buscarRegistros(char* nome_arq, Funcionario *ptrFuncionario){
    FILE *pFle;
    return 0;
}


int main(){

    char nome_arq[255] = "registros.bin";

    FILE *pFile = fopen(nome_arq, "wb");
    if(pFile == NULL)
    {
        printf("Erro ao criar o arquivo.\n");
    }
    fclose(pFile);

    Funcionario funcionario, *ptrFuncionario;
    ptrFuncionario = &funcionario;

    int menu;
    do
    {
        printf("\t1 - Adicionar Registros\n");
        printf("\t2 - Listar Registros\n");
        printf("\t3 - Buscar Registros\n");
        printf("\t0 - Sair\n");
        scanf("%d", &menu);

        switch (menu)
        {
        case 1:
            adicionarRegistros(nome_arq, ptrFuncionario);
            break;
        case 2:
            listarRegistros(nome_arq, ptrFuncionario);
            break;
        case 3:
            buscarRegistros(nome_arq, ptrFuncionario);
            break;
        case 0:
            exit(0);
            break;
        default:
            printf("Opcao invalida.\n");
            break;
        }
        
    }while (menu != 0);

    return 0;
}