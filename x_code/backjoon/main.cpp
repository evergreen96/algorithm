#include <stdio.h>
#include <stdlib.h>

#define TRUE 1
#define FALSE 0

typedef struct _NODE {
  char Data;
  struct _NODE* Left;
  struct _NODE* Right;
} NODE;


// �ܺ� �Լ� ����
extern void InitializeStack(void);
extern void Push(NODE*);
extern NODE* Pop(void);
extern int IsStackEmpty(void);

// ���� �Լ� ����
void InitializeTree(void);
void MakeTree(void);
void Recursive_Traverse(NODE*);
void Stack_Traverse(NODE*);
void Visit(NODE*);

// ���� ���� ����
NODE *Parent, *LeftChild, *RightChild, *HeadNode, *EndNode;

// Ʈ���� �ʱ�ȭ
void InitializeTree(void) {
  HeadNode = (NODE*)malloc(sizeof(NODE));
  EndNode = (NODE*)malloc(sizeof(NODE));

  HeadNode->Left = EndNode;
  HeadNode->Right = EndNode;

  EndNode->Left = EndNode;
  EndNode->Right = EndNode;
}

// Ʈ���� �ʱ� ����
void MakeTree(void) {
  Parent = (NODE*)malloc(sizeof(NODE));
  Parent->Data = 'A';

  LeftChild = (NODE*)malloc(sizeof(NODE));
  LeftChild->Data = 'B';

  RightChild = (NODE*)malloc(sizeof(NODE));
  RightChild->Data = 'C';

  Parent->Left = LeftChild;
  Parent->Right = RightChild;

  HeadNode->Left = Parent;
  HeadNode->Right = Parent;

  Parent = Parent->Left;

  LeftChild = (NODE*)malloc(sizeof(NODE));
  LeftChild->Data = 'D';
  LeftChild->Left = EndNode;
  LeftChild->Right = EndNode;

  RightChild = (NODE*)malloc(sizeof(NODE));
  RightChild->Data = 'E';
  RightChild->Left = EndNode;
  RightChild->Right = EndNode;

  Parent->Left = LeftChild;
  Parent->Right = RightChild;
  Parent = HeadNode->Right->Right;

  LeftChild = (NODE*)malloc(sizeof(NODE));
  LeftChild->Data = 'F';
  LeftChild->Left = EndNode;
  LeftChild->Right = EndNode;

  RightChild = (NODE*)malloc(sizeof(NODE));
  RightChild->Data = 'G';
  RightChild->Left = EndNode;
  RightChild->Right = EndNode;

  Parent->Left = LeftChild;
  Parent->Right = RightChild;
}

// ��� ȣ���� ����� Ʈ���� ��ȸ �˰�����
void Recursive_Traverse(NODE* ptrNode) {
  if (ptrNode != EndNode) {
    Recursive_Traverse(ptrNode->Left);
    Recursive_Traverse(ptrNode->Right);
    Visit(ptrNode);
  }
}

// ������ ����� Ʈ���� ��ȸ �˰�����
void Stack_Traverse(NODE* ptrNode) {
  int Finish = 0;
  NODE* ptrVisited = EndNode;
  NODE* ptrPushed = EndNode;

  do {
    while (ptrNode != EndNode && ptrNode != ptrVisited) {
      if (ptrNode != ptrPushed)
        Push(ptrNode);

      if (ptrNode->Right != EndNode)
        Push(ptrNode->Right);

      if (ptrNode->Left != EndNode)
        Push(ptrNode->Left);

      ptrPushed = ptrNode->Left;
      ptrNode = ptrNode->Left;
    }

    if (!IsStackEmpty()) {
      ptrNode = Pop();

      if (ptrNode->Left != EndNode && ptrNode->Right == EndNode &&
          ptrNode->Left != ptrVisited) {
        Push(ptrNode);
        ptrNode = ptrNode->Left;
      }

      if (ptrNode->Right == EndNode || ptrNode->Right == ptrVisited) {
        Visit(ptrNode);
        ptrVisited = ptrNode;
      }
    } else
      Finish = 1;
  } while (!Finish);
}

void Visit(NODE* ptrNode) { printf("%2c -> ", ptrNode->Data); }

int main() {
  InitializeStack(); // ������ �ʱ�ȭ
  InitializeTree();  // Ʈ���� �ʱ�ȭ
  MakeTree();        // Ʈ���� ����

  Recursive_Traverse(HeadNode->Left); // ��� ȣ��� Ʈ���� ��ȯ

  Stack_Traverse(HeadNode->Left);
}
