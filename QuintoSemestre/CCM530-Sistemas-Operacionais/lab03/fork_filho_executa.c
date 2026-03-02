#include <sys/types.h>
#include <stdio.h>
#include <sys/wait.h>
#include <unistd.h>

int main(){

	pid_t pid;
	/*fork de um processo filho*/

	pid = fork();
	printf("Meu pid: %d\n", pid);
	//se for filho
	if(pid == 0){
		execlp("/bin/ls", "ls", NULL);
	}
	else{ //pai espera o filho finalizar
		wait(NULL);
		printf("Filho Completo");
	}
	return 0;

}
