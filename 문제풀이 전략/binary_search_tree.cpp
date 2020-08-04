#include <iostream>

struct Node
{
    int key;
    Node *left;
    Node *right;
};

Node *head, *end;

void initialize()
{
    head->key = end->key = -1;
    head->left = head->right = end->left = end->right = end;
}

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

void deletetion(int num)
{
    Node *p, *c;
    p = head;
    c = head->right;
    while (c != end)
    {
        if (num < c->key)
        {
            p = c;
            c = c->left;
        }
        else if (num > c->key)
        {
            p = c;
            c = c->right;
        }
        else
        {
            break;
        }
    }
    if (c == end)
        return;
    Node *temp = c;
    if (c->left == NULL && c->right == NULL)
    {
        c = end;
    }
    else if (c->left != NULL && c->right == NULL)
    {
        c = c->left;
    }
    else if (c->left == NULL && c->right != NULL)
    {
        c = c->right;
    }
    else
    {
        Node *g = g->right;
        while (c->left->left != end)
        {
            g = g->left;
        }
        c = g->left;
        g->left = c->right;
        c->left = temp->left;
        c->right = temp->right;
    }
    delete temp;
    if (num > p->key)
        p->left = c;
    else
        p->right = c;
}

int main()
{
}