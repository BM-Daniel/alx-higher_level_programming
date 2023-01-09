#include "lists.h"
/**
 * is_palindrome - Write a function in C that checks if a singly
 * linked list is a palindrome
 * @head: Pointer to linked lists
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *current, *head2;
	int node = 0, divide, i = 0;

	current = *head;
	while (current != NULL)
	{
		node++;
		current = current->next;
	}
	divide = node / 2;
	head2 = *head;
	for (i = 0; i < divide; i++)
		head2 = head2->next;

	int array[divide];

	for (i = 0; i < divide; i++)
	{
		array[i] = head2->n;
		head2 = head2->next;
	}
	current = *head;
	for (divide = divide - 1; divide; divide--)
	{
		if (current->n != array[divide])
			return (0);
		current = current->next;
	}
	return (1);
}
