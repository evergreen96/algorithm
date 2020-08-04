#include <iostream>

struct Node
{
    int key;
    Node *left;
    Node *right;
};

Node *head, *end;

void insert(int num)
{
    Node *parent, *child;
    parent = head;
    child = head->right;

    while (child != end)
    {
        parent = child;
        child = (num < child->key) ? child->left : child->right;
    }
    child = new Node;
    child->key = num;
    child->left = end;
    child->right = end;

    if (num < parent->key)
        parent->left = child;
    else
        parent->right = child;
}

int main()
{
}