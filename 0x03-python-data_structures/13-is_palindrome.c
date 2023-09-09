#include "lists.h"
#include <stdbool.h>

/**
 * reverse - reverses a singly linked list
 * @head: double pointer to the head of the list
 */
void reverse(listint_t **head)
{
    listint_t *prev = NULL;
    listint_t *current = *head;
    listint_t *next;

    while (current != NULL)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    *head = prev;
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to the head of the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
    if (*head == NULL || (*head)->next == NULL)
    {
        return (1);
    }
    listint_t *slow = *head;
    listint_t *fast = *head;

    /*/ Find the middle of the linked list*/
    while (fast != NULL && fast->next != NULL)
    {
        slow = slow->next;
        fast = fast->next->next;
    }

    /*/ Reverse the second half of the linked list*/
    reverse(&slow);

    /* Compare the first half and the reversed second half*/
    while (slow != NULL)
    {
        if ((*head)->n != slow->n)
            return (0);

        *head = (*head)->next;
        slow = slow->next;
    }

    return (1);
}
