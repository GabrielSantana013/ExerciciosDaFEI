#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

#define SIZE 10 

int nums[SIZE] = {0,1,2,3,4,5,6,7,8,9};
int nums2[SIZE] = {10,9,8,7,6,5,4,3,2,1};

int main(){


	pid_t pid;
	int i;
	pid = fork();
	if(pid == 0){
		int nums_filho[SIZE];
		for(i = 0; i < SIZE; i++){
			nums_filho[i] = nums[i] + nums2[i];			
		}
		for(int i = 0; i < SIZE; i++){
			printf("%d ", nums_filho[i]);
		}
		printf("\nFim do filho\n");
	}
	else if(pid > 0){
		wait(NULL);
		int nums_pai[SIZE];
		for(i = 0; i < SIZE; i++){
			nums_pai[i] = nums[i] - nums2[i];
			printf("%d ", nums_pai[i]);
		}
		printf("Fim do pai\n");

	}
	return 0;

}
