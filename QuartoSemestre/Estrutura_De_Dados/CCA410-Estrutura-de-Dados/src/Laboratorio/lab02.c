#include <stdio.h>
#include <stdlib.h>

// Estrutura de uma célula da lista duplamente ligada
typedef struct Celula {
	int valor;					// Valor armazenado na célula
	struct Celula *proximo;		// Ponteiro para o próximo elemento
	struct Celula *anterior;	// Ponteiro para o elemento anterior
} Celula;

// Estrutura da fila com ponteiros para início e fim
typedef struct {
	Celula *head;	// Ponteiro para o primeiro elemento (início da fila)
	Celula *tail;	// Ponteiro para o último elemento (fim da fila)
	int qtde;		// Contador de elementos na fila
} Queue;

// Cria uma nova célula com o valor especificado
Celula *cria_celula(int valor){
	// Implementar
    Celula *cel = malloc(sizeof(Celula));
    cel->valor = valor;
    cel->proximo = NULL;
    cel->anterior = NULL;
    return cel;
}

// Cria uma nova fila vazia
Queue *cria_queue(){
	Queue *q = malloc(sizeof(Queue));
    q->head = NULL;
    q->tail = NULL;
    q->qtde = 0;
    return q;
}

// Operação ENQUEUE: insere elemento no final da fila (FIFO)
void enqueue(Queue *queue, int valor){
	// Implementar

    Celula *cel = cria_celula(valor);
    if(queue->tail == NULL && queue->head == NULL){
        queue->head = cel;
        queue->tail = cel;
    }else{
        queue->tail->proximo = cel;
        cel->anterior = queue->tail;
        queue->tail = cel;
    }
    queue->qtde++;
}

// Operação DEQUEUE: remove elemento do início da fila (FIFO)
int dequeue(Queue *queue){
	// Implementar
    if(queue->qtde == 0 || queue->head == NULL){
        return -1;
    }
    Celula *temp = queue->head;
    if(queue->head == queue->tail){
        queue->head = NULL;
        queue->tail = NULL;
    } else{
        queue->head = queue->head->proximo;
        queue->head->anterior = NULL;
    }
    int val = temp->valor;
    free(temp);
    queue->qtde--;
    return val;
}


// Exibe todos os elementos da fila (do início ao fim)
void show(Queue *queue){
	// Implementar
    Celula *atual = queue->head;
    while (atual != NULL)
    {
        printf("%d ", atual->valor);
        atual = atual->proximo;
    }
}


int main(void) {
	// Implementar

    int nums[] = {10,2,0,4,5,5,6,2,8,1,9};
    size_t nums_size = sizeof(nums)/sizeof(int); 
    Queue *fila = cria_queue();

    printf("=== INSERINDO ELEMENTOS ===");
    for(size_t i = 0; i < nums_size; i++){
        printf("\nInserido %d: ", nums[i]);
        enqueue(fila, nums[i]);
        show(fila);
    }

    printf("\n\n=== REMOVENDO ELEMENTOS ===");

    for(size_t i = 0; i < nums_size; i++){
        printf("\nValor removido: %d, Fila restante: ", nums[i]);
        dequeue(fila);
        show(fila);
    }
	
	return 0;
}