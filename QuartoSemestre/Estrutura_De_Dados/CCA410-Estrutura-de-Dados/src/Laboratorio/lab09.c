/*
 * Exercício: Percorrendo Grafos - Rede Social
 * Estrutura de Dados - Representação com Lista de Adjacência
 */

#include <stdio.h>
#include <stdlib.h>

// Estrutura do nó da lista
typedef struct No {
    int vertice;
    struct No *proximo;
} No;

// Estrutura do grafo
typedef struct {
    int numVertices;
    No **listaAdj;
} GrafoLista;

// ========== FUNÇÕES BÁSICAS DO GRAFO ==========

No* criarNo(int v) {
    No *novoNo = (No*)malloc(sizeof(No));
    novoNo->vertice = v;
    novoNo->proximo = NULL;
    return novoNo;
}

GrafoLista* criarGrafo(int n) {
    GrafoLista *grafo = (GrafoLista*)malloc(sizeof(GrafoLista));
    grafo->numVertices = n;
    grafo->listaAdj = (No**)malloc(n * sizeof(No*));
    
    for(int i = 0; i < n; i++) {
        grafo->listaAdj[i] = NULL;
    }
    return grafo;
}

void adicionarAresta(GrafoLista *grafo, int origem, int destino) {
    No *novoNo = criarNo(destino);
    novoNo->proximo = grafo->listaAdj[origem];
    grafo->listaAdj[origem] = novoNo;
    
    novoNo = criarNo(origem);
    novoNo->proximo = grafo->listaAdj[destino];
    grafo->listaAdj[destino] = novoNo;
}

void imprimirGrafo(GrafoLista *grafo) {
    printf("\n=== REDE SOCIAL ===\n");
    for(int i = 0; i < grafo->numVertices; i++) {
        No *temp = grafo->listaAdj[i];
        printf("Pessoa %d é amiga de:", i + 1);
        while(temp) {
            printf(" %d", temp->vertice + 1);
            temp = temp->proximo;
        }
        printf("\n");
    }
}

// ========== EXERCÍCIO 1: CONTADOR DE AMIGOS ==========

int contarAmigos(GrafoLista *grafo, int pessoa) {
    // implementar

    int amigos[] = {0, 0, 0, 0, 0, 0, 0};
    for(int i = 0; i < grafo->numVertices; i++) {
        No *temp = grafo->listaAdj[i];
        while(temp) {
            amigos[i]++;
            temp = temp->proximo;
        }
    }

    return amigos[pessoa - 1];

}

// ========== EXERCÍCIO 2: PESSOA MAIS POPULAR ==========

int pessoaMaisPopular(GrafoLista *grafo) {
    // implementar

    int popular = 0;

    //reaproveita a função anterior
    int amigos[] = {0, 0, 0, 0, 0, 0, 0};
    for(int i = 0; i < grafo->numVertices; i++) {
        No *temp = grafo->listaAdj[i];
        while(temp) {
            amigos[i]++;
            temp = temp->proximo;
        }
    }


    //percorre o vetor comparando pra ver quem tem mais amigos 
    for(int i = 0; i < (sizeof(amigos) / sizeof(amigos[0])); i++) {
        if(amigos[i] > amigos[popular]) {
            popular = i;
        }
    }

    return popular+1;

}

// ========== EXERCÍCIO 3: VERIFICAR AMIZADE DIRETA ==========

int saoAmigos(GrafoLista *grafo, int pessoa1, int pessoa2) {
    // implementar

    //cria um nó temporario que aponta para a lista de adjacência da pessoa1
    No *temp = grafo->listaAdj[pessoa1 - 1];
    while(temp){
        //se o vertice do nó temporario for igual a pessoa2 - 1 (ajuste de índice) é amigo
        if(temp->vertice == pessoa2 - 1){
            return 1;
        }
        temp = temp->proximo;
    }
    return 0;
}

// ========== EXERCÍCIO 4: AMIGOS EM COMUM ==========

/*========== EXERCÍCIO 4: AMIGOS EM COMUM ==========

Amigos em comum entre 1 e 3: 2 

Amigos em comum entre 2 e 4: 3 

Amigos em comum entre 5 e 6: 7 4 */


void amigosEmComum(GrafoLista *grafo, int pessoa1, int pessoa2) {
    // implementar
    
    //percorro 1 e 2, se a soma dos dois for igual a 2, é amigo em comum
    int amigos[] = {0, 0, 0, 0, 0, 0, 0};

    No *temp = grafo->listaAdj[pessoa1 - 1];
    while(temp) {
        amigos[temp->vertice]++;
        temp = temp->proximo;
    }   

    temp = grafo->listaAdj[pessoa2 - 1];
        while(temp) {
        amigos[temp->vertice]++;
        temp = temp->proximo;
    }
    printf("\n");
    printf("Amigos em comum entre %d e %d: ", pessoa1, pessoa2);
    
    for(int i = grafo->numVertices -1; i > 0; i--) {
        if(amigos[i] == 2) {
            printf("%d ", i + 1);
            
        }
    }
    printf("\n");
    
}

// ========== EXERCÍCIO 5: RECOMENDAÇÃO DE AMIZADE ==========


void recomendarAmigos(GrafoLista *grafo, int pessoa) {
    // implementar


    //se a soma dos amigos for igual a 1, é amigo de amigo
    int amigos[] = {0, 0, 0, 0, 0, 0, 0};
    int amigos_dos_amigos[] = {0, 0, 0, 0, 0, 0, 0};

    No *temp = grafo->listaAdj[pessoa - 1];
    while(temp) {
        amigos[temp->vertice]++;
        temp = temp->proximo;
    }

    //precisa percorrer os amigos da pessoa somando no vetor amigos
    // Para cada amigo direto da pessoa, marque no vetor amigos
    temp = grafo->listaAdj[pessoa - 1];
    while (temp) {
        int amigo = temp->vertice;
        // Para cada amigo do amigo
        No *temp2 = grafo->listaAdj[amigo];
        while (temp2) {
            int possivel = temp2->vertice;
            // Não recomenda a própria pessoa nem quem já é amigo direto
            if (possivel != (pessoa - 1) && amigos[possivel] == 0 && amigos_dos_amigos[possivel] == 0) {                
                amigos_dos_amigos[possivel] = amigo + 1; // guarda quem é o amigo em comum
            }
            temp2 = temp2->proximo;
        }
        temp = temp->proximo;
    }

    //imprime os amigos de amigos
    printf("\n");
    printf("Recomendações de amizade para pessoa %d:\n", pessoa);
    for(int i = grafo->numVertices-1; i > 0 ; i--) {
        if(amigos_dos_amigos[i] > 1) {
            printf("  -> Pessoa %d (amiga de %d)\n", i +
                     //encontra quem é o amigo em comum
                     1, amigos_dos_amigos[i]);
        }
    }

}

// ========== FUNÇÃO PRINCIPAL ==========

int main() {
    // Cria o grafo fixo da rede social
    GrafoLista *grafo = criarGrafo(7);
    
    // Define as amizades (grafo fixo)
    adicionarAresta(grafo, 0, 1);  // Pessoa 1 - 2
    adicionarAresta(grafo, 0, 2);  // Pessoa 1 - 3
    adicionarAresta(grafo, 1, 2);  // Pessoa 2 - 3
    adicionarAresta(grafo, 2, 3);  // Pessoa 3 - 4
    adicionarAresta(grafo, 2, 4);  // Pessoa 3 - 5
    adicionarAresta(grafo, 3, 4);  // Pessoa 4 - 5
    adicionarAresta(grafo, 3, 5);  // Pessoa 4 - 6
    adicionarAresta(grafo, 4, 5);  // Pessoa 5 - 6
    adicionarAresta(grafo, 4, 6);  // Pessoa 5 - 7
    adicionarAresta(grafo, 5, 6);  // Pessoa 6 - 7
    
    // Exibe a rede social
    imprimirGrafo(grafo);
    
    // ========== TESTES DOS EXERCÍCIOS ==========
    
    printf("\n========== EXERCÍCIO 1: CONTADOR DE AMIGOS ==========\n");
    for(int i = 1; i <= 7; i++) {
        printf("Pessoa %d tem %d amigo(s)\n", i, contarAmigos(grafo, i));
    }
    
    printf("\n========== EXERCÍCIO 2: PESSOA MAIS POPULAR ==========\n");
    int popular = pessoaMaisPopular(grafo);
    printf("A pessoa mais popular é %d com %d amigos\n", 
           popular, contarAmigos(grafo, popular));
    
    printf("\n========== EXERCÍCIO 3: VERIFICAR AMIZADE ==========\n");
    printf("Pessoa 1 e 2 são amigas? %s\n", 
           saoAmigos(grafo, 1, 2) ? "SIM" : "NÃO");
    printf("Pessoa 1 e 4 são amigas? %s\n", 
           saoAmigos(grafo, 1, 4) ? "SIM" : "NÃO");
    printf("Pessoa 5 e 7 são amigas? %s\n", 
           saoAmigos(grafo, 5, 7) ? "SIM" : "NÃO");
    
    printf("\n========== EXERCÍCIO 4: AMIGOS EM COMUM ==========\n");
    amigosEmComum(grafo, 1, 3);
    amigosEmComum(grafo, 2, 4);
    amigosEmComum(grafo, 5, 6);
    
    printf("\n========== EXERCÍCIO 5: RECOMENDAÇÃO DE AMIZADE ==========\n");
    recomendarAmigos(grafo, 1);
    recomendarAmigos(grafo, 7);
    
    printf("\n");
    return 0;
}