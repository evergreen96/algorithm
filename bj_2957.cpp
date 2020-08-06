// 이진 탐색 트리


//시간 초과
#include <iostream>
using namespace std;

struct Node
{
    int num=-1;
    Node *left=NULL;
    Node *right=NULL;
};

void insert(int &count, int num, Node *node);

int main()
{

    int loop;
    cin >> loop;
    int num;
    Node *root = new Node;
    int count = 0;
    for(int i=0; i<loop; i+    +)
    {
        c>> num;
       // if(i !=0)            ;
        insert(count, num, root);
    }
}

void insert(int &count, int num, Node *node)
{
    if (node->num == -1)
    {
        cout << count << endl;
        node->num = num;
    }
    else if (node->num > num)
    {
        if (node->left == NULL)
        {
            Node *temp= new Node;
            temp->num = num;
            node->left = temp;
            count++;
            cout<<count<<endl;

        }
        
        els    ins(                  t);
         {        (n  ULL)
        {
                     temp->nu         node->ri                    count++;         cout<<co                  
 e        de->right);
        }
    }
}     
