#include <stdio.h>
#include <stdlib.h>

#define grafos_pesos

#ifdef grafos_n_ponderados

int main(){
/* input
    1 2
    1 3
    2 3
    3 4
    3 5
    4 5
    4 6
    5 6
    5 7
    6 7
  */  

    //alocar memoria pros vertices
    printf("GRAFOS NAO PONDERADOS\n");
    int n, **vertices, arestas;
    printf("Digite o numero de vertices: ");
    scanf("%d", &n);
    vertices = malloc(n * sizeof(int*));
    for (int i = 0; i < n; i++) {
        vertices[i] = malloc(n * sizeof(int));
    }

    //inicializar matriz com 0
    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            vertices[i][j] = 0;
        }
    }

    //input do tipo 1 2
    printf("Digite quantas arestas: \n");
    scanf("%d", &arestas);
    for (int i = 0; i < arestas; i++) {
        int u, v;
        scanf("%d %d", &u, &v);
        u--; v--; // ajustar para índice baseado em 0
        vertices[u][v] = 1;
        vertices[v][u] = 1;
    }

    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            printf("%d ", vertices[i][j]);
        }
        printf("\n");
    }

    return 0;
}

#endif


#ifdef grafos_ponderados

int main(){
/* input
    1 3
    2 1
    2 3
    3 5
    4 3
    4 5
    5 6
    6 4
    6 7
    7 5
  */  

    //alocar memoria pros vertices
    printf("GRAFOS PONDERADOS\n");
    int n, **vertices, arestas;
    printf("Digite o numero de vertices: ");
    scanf("%d", &n);
    vertices = malloc(n * sizeof(int*));
    for (int i = 0; i < n; i++) {
        vertices[i] = malloc(n * sizeof(int));
    }

    //inicializar matriz com 0
    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            vertices[i][j] = 0;
        }
    }

    //input do tipo 1 2
    printf("Digite quantas arestas: \n");
    scanf("%d", &arestas);
    for (int i = 0; i < arestas; i++) {
        int u, v;
        scanf("%d %d", &u, &v);
        u--; v--; // ajustar para índice baseado em 0
        vertices[u][v] = 1;
    }

    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            printf("%d ", vertices[i][j]);
        }
        printf("\n");
    }

    return 0;
}
#endif

#ifdef grafos_pesos

int main(){
/* input
    1 2 1
    1 3 5
    2 3 4
    3 4 2
    3 5 1
    4 5 4
    4 6 3
    5 6 3
    5 7 2
    6 7 4
  */  

    //alocar memoria pros vertices
    printf("GRAFOS PONDERADOS\n");
    int n, **vertices, arestas;
    printf("Digite o numero de vertices: ");
    scanf("%d", &n);
    vertices = malloc(n * sizeof(int*));
    for (int i = 0; i < n; i++) {
        vertices[i] = malloc(n * sizeof(int));
    }

    //inicializar matriz com 0
    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            vertices[i][j] = 0;
        }
    }

    //input do tipo 1 2
    printf("Digite quantas arestas: \n");
    scanf("%d", &arestas);
    for (int i = 0; i < arestas; i++) {
        int u, v, peso;
        scanf("%d %d %d", &u, &v, &peso);
        u--; v--; // ajustar para índice baseado em 0
        vertices[u][v] = peso;
        vertices[v][u] = peso;
    }

    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            printf("%d ", vertices[i][j]);
        }
        printf("\n");
    }

    return 0;
}
#endif