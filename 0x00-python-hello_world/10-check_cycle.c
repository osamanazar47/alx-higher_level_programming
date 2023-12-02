#include <stdio.h>
#include "lists.h"
/*
 * check_cycle - check if there is a cycle in the linked lists
 * @list: the list
 * Return: an integer
 */
int check_cycle(listint_t *list)
{
	listint_t *hare, *tortoise;

	tortoise = list;
	hare = list;
	while (hare && hare->next)
	{
		hare = hare->next->next;
		tortoise = tortoise->next;
		if (tortoise == hare)
			return (1);
	}
	return (0);
}
