#include "lists.h"

/**
 * reverse_listint - reverses a linked list
 * @head: pointer to the first node in the list
 * Return: pointer to the first node in the new list
 */
void reverse_listint(listint_t **head)
{
	listint_t *last_node = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = last_node;
		last_node = current;
		current = next;
	}

	*head = last_node;
}

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: double pointer to the linked list
 *
 * Return: 1 if it is, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *temp = *head, *second_half = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (1)
	{
		fast = fast->next->next;
		if (!fast)
		{
			second_half = slow->next;
			break;
		}
		if (!fast->next)
		{
			second_half = slow->next->next;
			break;
		}
		slow = slow->next;
	}

	reverse_listint(&second_half);

	while (second_half && temp)
	{
		if (temp->n == second_half->n)
		{
			second_half = second_half->next;
			temp = temp->next;
		}
		else
			return (0);
	}

	if (!second_half)
		return (1);

	return (0);
}
