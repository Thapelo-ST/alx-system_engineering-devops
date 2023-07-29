#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

/**
 * infinite_while - loop that never stops
 * Return: ...
 */

int infinite_while(void)
{
	while (1)
		sleep(1);

	return (0);
}

/**
 * main - code entry point
 * Return: ...
 */

int main(void)
{
	/* declare variables */
	pid_t child_pid;
	int i;

	/* loop for creating zombies */
	for (i = 0; i < 5; i++)
	{
		child_pid = fork();

		if (child_pid == -1)
		{
			perror("fork");
			exit(1);
		}

		if (child_pid == 0)
			exit(0);
		else
			printf("Zombie proccess created, PID: %d\n", child_pid);
	}

	infinite_while();
	return (0);
}
