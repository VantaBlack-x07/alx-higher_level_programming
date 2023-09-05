#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 *
 * @list - list to be checked
 *
 * Return: 1 if there is a cycle, or 0 if not.
 */

int check_cycle(listint_t *list)
{
	listint_t *fast_node, *slow_node;

	fast_node = list;
	slow_node = list;

	while (1)
	{
		fast_node = fast_node->next->next;
		slow_node = slow_node->next;

		if (fast_node == slow_node || slow_node == list)
			return (1);
		if (fast_node == NULL || fast_node->next == NULL)
			return (0);
	}
}
