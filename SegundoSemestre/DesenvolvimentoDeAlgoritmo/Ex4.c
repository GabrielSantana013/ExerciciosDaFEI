//Operações Matriciais: Implemente funções para multiplicação de matrizes e transposição.
//Utilize ponteiros para alocar dinamicamente o espaço de memória.

#include <stdio.h>
#include <stdlib.h>

int ** alocar(int n, int m){

    int **matriz;
    matriz = (int**) malloc(n * sizeof(int*));
    //verifica erro
    if(matriz == NULL)
    {
        printf("Erro ao alocar a matriz.\n");
        return 1;
    }
    else
    {
        for(int i = 0; i < n; i++)
        {
            matriz[i] = (int*) malloc(m * sizeof(int));
            //verifica erro
            if(matriz[i] == NULL)
            {
                printf("Erro ao alocar a matriz.\n");
                return 1;
            }
        }
    }

    for(int i = 0; i < n; i++)
    {
        for(int j = 0; j < m; j++)
        {
            printf("Digite o numero da posicao [%d][%d]", i,j);
            scanf("%d", &matriz[i][j]);
        }
    }

    for(int i = 0; i < n; i++)
    {
        for(int j = 0; j < m; j++)
        {
            printf("%d", matriz[i][j]);
        }
    }
    return matriz;
}


int multiplicar(int n, int m, int **matriz1, int**matriz2){
    printf("\n\n");
    
    for(int i = 0; i <n; i++)
    {
        for(int j = 0; j < m; j++)
        {
            printf("%d ", matriz1[i][j] * matriz2[j][i]);
        }
        printf("\n");
    }

    return 0;
}

int transpor(int n, int m, int **matriz)
{
    
    int **matrizTransposta;
    matrizTransposta = (int**) malloc(m * sizeof(int*));

   if(matrizTransposta == NULL)
    {
        printf("Erro ao alocar a matriz.\n");
        return 1;
    }
    else
    {
        for(int i = 0; i < m; i++)
        {
            matrizTransposta[i] = (int*) malloc(n * sizeof(int));
            //verifica erro
            if(matrizTransposta[i] == NULL)
            {
                printf("Erro ao alocar a matriz.\n");
                return 1;
            }
        }
    }

    for(int i = 0; i < n; i++)
    {
        for(int j = 0; j<m; j++)
        {
            matrizTransposta [j][i] = matriz[i][j];
        }
    }

    for(int i = 0; i < m; i++)
    {
        for(int j = 0; j<n; j++)
        {
            printf("%d ", matrizTransposta [i][j]);
        }
        printf("\n");
    }
    
    return 0;
}


int main(){

    int **matriz1, **matriz2;
    int n, m;

    int menu;
    do
    {
        printf("\t1 - Alocar matriz\n");
        printf("\t2 - Multiplicar matriz\n");
        printf("\t3 - Transpor matriz\n");
        printf("\t0 - Sair\n");
        scanf("%d", &menu);

        switch (menu)
        {
        case 1:
            printf("Digite o numero de colunas: ");
            scanf("%d", &n);
            printf("Digite o numero de linhas: ");
            scanf("%d", &m);
            matriz1 = alocar(n,m);
            break;
        case 2:
            matriz2 = alocar(n,m);
            multiplicar(n, m, matriz1,matriz2);
            break;
        case 3:
            transpor(n,m,matriz1);
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