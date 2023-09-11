#include "lists.h"

/**
 * reversedLinkedList - checks if a singly linked list is a palindrome.
 *
 * @head: The head of the list
 *
 * Return: The reversed linked list.
 */

listint_t reversedLinkedList(listint_t *head)
{
	listint_t *prev = NULL;
	listint_t *current = head;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	return (prev);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 *
 * @head: The head of the list.
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 */

int is_palindrome(listint_t **head)
{
	listint_t *reversed = reversedLinkedList(head);

	while (head != NULL && reversed != NULL)
	{
		if (head->n != reversed->n)
			return (false);

		head = head->next;
		reversed = reversed->next;
	}

	return (head == NULL && reversed == NULL)
}
