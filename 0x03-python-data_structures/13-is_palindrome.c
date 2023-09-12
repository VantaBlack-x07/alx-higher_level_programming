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
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

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
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *second_half = NULL;

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		slow = slow->next;
	}

	if (fast != NULL)
	{
		slow = slow->next;
	}

	second_half = reversedLinkedList(&slow);

	while (second_half != NULL)
	{
		if ((*head)->n != second_half->n)
		{
			return (0);
		}
		*head = (*head)->next;
		second_half = second_half->next;
	}

	return (1);
}
