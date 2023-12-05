#include "lists.h"
/**
 * is_palindrome - checks if the linked lists is a palindrome
 * @head: a pointer to a pointer to the first node
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *first = *head, *second = *head;
	listint_t *nextnode, *previous = NULL;

	while (first != NULL && first->next != NULL)
	{
		first = first->next->next;
		second = second->next;
	}
	while (second != NULL)
	{
		nextnode = second->next;
		second->next = previous;
		previous = second;
		second = nextnode;
	}
	while (previous != NULL && *head != NULL)
	{
		if (previous->n != (*head)->n)
			return (0);
		previous = previous->next;
		*head = (*head)->next;
	}
	return (1);
}
