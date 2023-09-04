#include "lists.h"

/**
 * check_cycle - function checks if a singly linked list has a cycle in it.
 * @list: pointer to the beginning of the node
 * Return: 0 if no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
    listint_t *current, *to_visit;
    if (list != NULL && list->next != NULL)
    {
        current = list;
        to_visit = current->next;

        while(current != NULL && to_visit->next != NULL && to_visit->next->next != NULL)
        {
            if (current == to_visit)
            {
                return (1);
            }
                current = current->next;
                to_visit = to_visit->next->next;
        }
    }
    return (0);
}
