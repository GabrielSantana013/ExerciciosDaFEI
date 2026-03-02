#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>

int main(){

	printf("ola\n");
	//faz os dois processos executarem o mesmo programa após
	//essa instrução
	fork();

	printf("Hello World!\n");
	return 0;

}
