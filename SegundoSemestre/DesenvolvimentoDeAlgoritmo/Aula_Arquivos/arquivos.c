#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int escreverArquivo(char *nome_arq){



return 0;
}



int lerArquivo(char *nome_arq){

    char linha [255];
    FILE *pFile = fopen(nome_arq, "r");
    int bytes = sizeof(pFile);

    if(pFile == NULL)
    {
        printf("Erro ao abrir o arquivo! \n");
        return 1;
    }
    
    //feof lê até achar o EOF.
    while(!feof(pFile))
    {
        fgets(linha, sizeof(linha), pFile);
        printf("%s", linha);
    }
    rewind(pFile);

    //pode ser assim tbm
    // while(fread(nome_arq, sizeof(pFile), 1, pFile) == 1)
    // {
    //     fgets(linha, sizeof(linha), pFile);
    //     printf("%s", linha);
    // }

    //Pra contar as linhas:
    int linhas = 0;
    while(!feof(pFile))
    {
        //aqui eu não consegui fazer de outro jeito sem usar o fgets
        fgets(linha, sizeof(linha), pFile);
        linhas++;
    }
    printf("O arquivo tem %d linhas", linhas);

    fclose(pFile);
    

    return 0;
}



int main(){

    char arquivo[255] = "arquivo.txt";
    lerArquivo(arquivo);

    return 0;
}