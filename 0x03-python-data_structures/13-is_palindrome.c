#include "lists.h"

/**
 * reversedLinkedList - Reverses a singly linked list.
 *
 * @head: The head of the list.
 *
 * Return: The reversed linked list.
 */
listint_t *reversedLinkedList(listint_t **head)
{
	listint_t *prev, *current, next;

	prev = NULL;
	current = *head;
	next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
	return (prev);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 *
 * @head: The head of the list.
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 */
int is_palindrome(listint_t **head)
{
	listint_t *reversed, *tmp, *temp_reversed;

	if (*head == NULL) {
		return 0;
	}

	reversed = NULL;
	reversed = reversedLinkedList(head);
	temp = *head;
	temp_reversed = reversed;

	while (temp != NULL && temp_reversed != NULL)
	{
		if (temp->n != temp_reversed->n)
			return (0);
		temp = temp->next;
		temp_reversed = temp_reversed->next;
	}

	return (temp == NULL && temp_reversed == NULL);
}
