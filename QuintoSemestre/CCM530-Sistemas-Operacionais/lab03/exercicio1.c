#include <sys/types.h>
#include <stdio.h>
#include <sys/wait.h>
#include <unistd.h>

int main(){


	pid_t pid;
	pid = fork();
	printf("Meu pid: %d\n",pid);

	if(pid == 0){
		printf("Filho escrevendo:\n");
		execlp("python3", "python3", "ex1_input.py", NULL);
	}
	else{
		wait(NULL);
		printf("Pai lendo:\n");
		execlp("python3", "python3", "ex1_output.py", NULL);
	}


	return 0;
}
