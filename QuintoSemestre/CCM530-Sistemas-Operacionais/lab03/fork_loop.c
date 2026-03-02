#include <stdio.h>
#include <unistd.h>

int main(){

	int i, p;
	int max = 3;

	for(i = 0; i < max; i++){
		p = fork();
	}
	printf("%d\n", p);
	return 0;


	return 0;
}
