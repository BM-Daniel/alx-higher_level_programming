#include "lists.h"

/**
 * check_cycle - Write a function in C that checks if a singly linked
 * list has a cycle in it
 * @list: Pointer to linked list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *headcopy;

	headcopy = list;
	list = list->next;

	if (list == NULL || list->next == NULL)
		return (0);

	while (list != NULL)
	{
		if (list == headcopy)
			return (1);

		list = list->next;
	}

	return (0);
}
