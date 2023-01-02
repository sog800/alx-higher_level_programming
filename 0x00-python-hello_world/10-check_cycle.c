#include "lists.h"

/**
 * check_cycle - checking for cycle in a linked list
 * @list: head ponter
 *
 * Return: return 1 for cycle, 0 without a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *fast;
	listint_t *slow;

	if (list == NULL)
	{
		return (0);
	}
	if (list->next == NULL)
	{
		return (0);
	}
	fast = list;
	slow = list;

	while (fast != NULL)
	{
		fast = fast->next->next;
		slow = slow->next;
		if (fast == slow)
		{
			return (1);
		}
		if (fast == NULL)
			return (0);
	}
	return (0);
}
