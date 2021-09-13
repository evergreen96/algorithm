#include <stdio.h>
#include <stdlib.h>

#define TRUE 1
#define FALSE 0

typedef struct _NODE
{
  char Data;
  struct _NODE *Left;
  struct _NODE *Right;
} NODE;
NODE *HeadNode, *EndNode;

#define MAX 100

NODE *Stack[MAX]; // ������ �迭�� ����
int Top;

void InitializeStack(void);
void Push(NODE *);
NODE *Pop(void);
int IsStackEmpty(void);

// ���� �ʱ�ȭ �Լ�
void InitializeStack(void)
{
  Top = 0;
}

void Push(NODE *ptrNode)
{
  Stack[Top] = ptrNode;
  Top = Top % MAX;
  Top++;
}

NODE *Pop(void)
{
  NODE *ptrNode;

  if (!IsStackEmpty())
  {
    ptrNode = Stack[--Top];

    return ptrNode;
  }

  else
    printf("Stack is Empty\n");

  return NULL;
}

int IsStackEmpty(void)
{
  if (Top == 0)
    return TRUE;

  else
    return FALSE;
}

// �ܺ� �Լ� ����
extern void InitializeStack(void);
extern void Push(NODE *);
extern NODE *Pop(void);
extern int IsStackEmpty(void);

// ���� �Լ� ����
void InitializeTree(void);
void MakeTree(void);
void Recursive_Traverse(NODE *);
void Stack_Traverse(NODE *);
void Visit(NODE *);

void Recursive_Traverse(NODE *ptrNode)
{
  if (ptrNode != EndNode)
  {
    Recursive_Traverse(ptrNode->Left);
    Recursive_Traverse(ptrNode->Right);
    Visit(ptrNode);
  }
}

// ���� ���� ����
NODE *Parent, *LeftChild, *RightChild, *HeadNode, *EndNode;

// Ʈ���� �ʱ�ȭ
void InitializeTree(void)
{
  HeadNode = (NODE *)malloc(sizeof(NODE));
  EndNode = (NODE *)malloc(sizeof(NODE));

  HeadNode->Left = EndNode;
  HeadNode->Right = EndNode;

  EndNode->Left = EndNode;
  EndNode->Right = EndNode;
}

// Ʈ���� �ʱ� ����
void MakeTree(void)
{
  Parent = (NODE *)malloc(sizeof(NODE));
  Parent->Data = 'A';
  LeftChild = (NODE *)malloc(sizeof(NODE));
  LeftChild->Data = 'B';
  RightChild = (NODE *)malloc(sizeof(NODE));
  RightChild->Data = 'C';
  Parent->Left = LeftChild;
  Parent->Right = RightChild;
  HeadNode->Left = Parent;
  HeadNode->Right = Parent;
  Parent = Parent->Left;
  LeftChild = (NODE *)malloc(sizeof(NODE));
  LeftChild->Data = 'D';
  LeftChild->Left = EndNode;
  LeftChild->Right = EndNode;
  RightChild = (NODE *)malloc(sizeof(NODE));
  RightChild->Data = 'E';
  RightChild->Left = EndNode;
  RightChild->Right = EndNode;
  Parent->Left = LeftChild;
  Parent->Right = RightChild;

  Parent = HeadNode->Right->Right;
  LeftChild = (NODE *)malloc(sizeof(NODE));
  LeftChild->Data = 'F';
  LeftChild->Left = EndNode;
  LeftChild->Right = EndNode;
  RightChild = (NODE *)malloc(sizeof(NODE));
  RightChild->Data = 'G';
  RightChild->Left = EndNode;
  RightChild->Right = EndNode;
  Parent->Left = LeftChild;
  Parent->Right = EndNode;

  Parent = Parent->Left;
  LeftChild = (NODE *)malloc(sizeof(NODE));
  LeftChild->Data = 'G';
  LeftChild->Left = EndNode;
  LeftChild->Right = EndNode;
  Parent->Left = LeftChild;
  Parent->Right = EndNode;
}

// ������ ����� Ʈ���� ��ȸ �˰�����
void Stack_Traverse(NODE *ptrNode)
{
  int Finish = 0;
  NODE *ptrVisited = EndNode, *ptrPushed = EndNode;
  printf("start\n");
  do
  {
    while (ptrNode != EndNode && ptrNode != ptrVisited) // 이미 방문했거나 엔드노드가 아니라면 스택에 넣는다.
    {
      if (ptrNode != ptrPushed)
      {
        Push(ptrNode);
      }
      if (ptrNode->Right != EndNode)
      {
        Push(ptrNode->Right);
      }
      if (ptrNode->Left != EndNode)
      {
        Push(ptrNode->Left);
      }
      ptrPushed = ptrNode->Left;
      ptrNode = ptrNode->Left;
    }
    if (!IsStackEmpty())
    {
      ptrNode = Pop();
      //printf("%c\n", ptrNode->Data);
      if (ptrNode->Left != EndNode && ptrNode->Right == EndNode && ptrNode->Left != ptrVisited)
      {
        Push(ptrNode);
        ptrNode = ptrNode->Left;
      }
      if (ptrNode->Right == EndNode || ptrNode->Right == ptrVisited)
      {
        Visit(ptrNode);
        ptrVisited = ptrNode;
      }
    }
    else
    {
      Finish = 1;
    }
  } while (!Finish);
}

void Visit(NODE *ptrNode)
{
  printf("%2c -> ", ptrNode->Data);
}

int main()
{
  InitializeStack(); // ������ �ʱ�ȭ
  InitializeTree();  // Ʈ���� �ʱ�ȭ
  MakeTree();        // Ʈ���� ����

  Recursive_Traverse(HeadNode->Left);

  Stack_Traverse(HeadNode->Left);
}
