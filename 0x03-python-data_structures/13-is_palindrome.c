#include "lists.h"
/**
 * list_length - finds the length of a singly linked list
 * @head: pointer to the head of the list
 * Return: the length of the list
 */
int list_length(listint_t **head)
{
    listint_t *current = *head;
    int len = 0;

    while (current)
    {
        len++;
        current = current->next;
    }

    return (len);
}
/**
 * is_palindrome - function that checks if a singly linked list is a palindrome
 * @head: Pointer to head
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
    listint_t *curr = *head;
    int len = 0, i, odd_flag = 0;
    int *nums;

    if (head && (*head) && (*head)->next)
    {
        len = list_length(head);
        if (len % 2)
        {
            len = len + 1;
            odd_flag = 1;
        }
        nums = malloc(sizeof(int) * len);
        if (!nums)
        {
            return (0);
        }
        curr = *head;
        for (i = 0; i < (len/2); i++)
        {
            nums[i] = curr->n;
            curr = curr->next;            
        }
        if (odd_flag)
        {
            i = i - 2;
        }
        else
        {
            i = i - 1;
        }
        for (; i >= 0; i--, curr = curr->next)
        {
            if (nums[i] != curr->n)
            {
                free(nums);
                return (0);
            }
        }
        free(nums);
        return (1);
    }
    return (1);
}
