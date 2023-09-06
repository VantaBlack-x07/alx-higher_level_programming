#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list.
 *
 * @head: The head of the list.
 * @number: The value of the node.
 *
 * Return: The address of the new node, or NULL if it failed.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp_node, *new_node, *prev_node;

	tmp_node = *head;
	prev_node = NULL;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL)
	{
		*head = new_node;
		return new_node;
	}

	while (tmp_node != NULL && tmp_node->n < number)
	{
		prev_node = tmp_node;
		tmp_node = tmp_node->next;
	}

	if (prev_node == NULL)
	{
		new_node->next = *head;
		*head = new_node;
	}
	else
	{
		prev_node->next = new_node;
		new_node->next = tmp_node;
	}

	return (new_node);
}
