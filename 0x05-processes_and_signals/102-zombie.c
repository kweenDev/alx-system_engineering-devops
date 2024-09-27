#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

/**
* create_zombies - Creates 5 zombie processes
*/
void create_zombies(void)
{
	pid_t pid;
	int i;

	for (i = 0; i < 5; i++)
	{
		pid = fork();

		if (pid < 0)
		{
			perror("Fork failed");
			exit(EXIT_FAILURE);
		}
		else if (pid == 0)
		{
			/* Child process */
			exit(EXIT_SUCCESS);
		}
		else
		{
			/* Parent process */
			printf("Zombie process created, PID: %d\n", pid);
			sleep(1);
		}
	}
}

/**
* infinite_while - Runs an infinite loop
*
* Return: Always returns 0
*/
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
* main - Entry point
*
* Return: Always returns 0
*/
int main(void)
{
	create_zombies();
	/* This function keeps the program running */
	infinite_while();

	return (0);
}
