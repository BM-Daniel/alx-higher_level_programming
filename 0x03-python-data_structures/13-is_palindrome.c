#include "lists.h"
/**
 * i_palindrome - Write a function in C that checks if a singly
 * linked list is a palindrome
 * @head: Pointer to linked lists
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *current;
	int nodes = 0, i = 0;

	if (*head == NULL)
		return (1);

	current = *head;
	while (current != NULL)
	{
		nodes++;
		current = current->next;
	}

	int array[nodes];

	current = *head;
	for (i = 0; i < nodes; i++)
	{
		array[i] = current->n;
		current = current->next;
	}

	for (i = 0; i < nodes; i++)
	{
		if (array[i] != array[nodes - 1])
			return (0);
		nodes--;
	}
	return (1);
}
