#include "lists.h"
/**
 * insert_node - fxn to insert Num in list
 * @head: start of list
 * @number: to insert
 * Return: new node address or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current;
	listint_t *new;

	current = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
	{
		return (NULL);
	}
	new->n = number;
	new->next = NULL;

	if (*head == NULL)
	{
		*head = new;
	}
	else
	{
		while ((current->next != NULL) && (current->n < number))
		{
			current = current->next;
		}
		new->next = current->next;
		current->next = new;
	}
	return (new);
}
