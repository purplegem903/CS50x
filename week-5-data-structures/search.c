// Searching a Binary Search Tree

#include <stdio.h>
#include <stdlib.h>

bool search(node *tree, int number);

int main(void)
{
}

bool search(node *tree, int number)
{
    if (tree == NULL)
    {
        return false;
    }
    else if (number < tree->number)
    {
        return search(tree->left, number);
    }
    else if (number > tree->number)
    {
        return search(tree->right, number);
    }
    else
    {
        return true;
    }
}