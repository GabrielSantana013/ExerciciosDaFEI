#include <stdio.h>
#include <stdlib.h>

typedef struct{
    int *data;
    int size;
    // num of elements inside heap;
    int count;

}Heap;

Heap *create_heap(int size){

    Heap *heap = malloc(sizeof(Heap));
    heap->data = malloc(size * sizeof(int));
    heap->size = size;
    heap->count = 0;
    return heap;
}

void heapify_up(Heap *heap, int childIndex){

    if(childIndex<=0){
        return;
    }

    int parentIndex = (childIndex-1) /2;

    if(heap->data[childIndex] > heap->data[parentIndex]){
        int temp = heap->data[childIndex];
        heap->data[childIndex] = heap->data[parentIndex];
        heap->data[parentIndex] = temp;

        heapify_up(heap, parentIndex);
    }

}

void heapify_down(Heap *heap, int parentIndex){

    

}


void insert(Heap *heap, int value){

    if(heap->count >= heap->size){
        return;
    }

    heap->data[heap->count] = value;
    heapify_up(heap, heap->count);
    heap->count++;
}

void pop(Heap *heap){

    if(heap->count < 0){
        return;
    }

    heap->data[0] = heap->data[heap->count-1];
    heap->count--;
    if(heap->count>0){
        heapify_down(heap,0);
    }
}


int main(){


    return 0;
}