#include<iostream>
#include<vector>
#include<sstream>
#include<cstring>
#include<string>
using namespace std;
#define RED 1
#define BLACK 0

class Node{
public:
    int color;
    Node* left;
    Node*  right;
    Node* parent;
    int number;
    string name;
    string phone;
    int x;
    int y;
    vector<string> v_illness;
    vector<int> v_cost;
    int depth;
    bool isNew;
    
    // init
    Node():v_illness(10), v_cost(10){
        color = RED;
        left = nullptr; right =  nullptr; parent = nullptr;
        v_illness.clear();
        v_cost.clear();
        depth=-1;
        isNew = true;
    }
    // value set
    void set(int K, string N, string H, int Ax, int Ay, string DI, int C){
        this->number = K;
        this->name = N;
        this->phone = H;
        this->x = Ax;
        this->y = Ay;
        v_illness.push_back(DI);
        v_cost.push_back(C);
    }
};

class Tree{
public:
    Node* root;

    Tree(){
        root = nullptr;
    }

    Node* insert(int K, string N, string H, int Ax, int Ay, string DI, int C){
        Node* newNode  = new Node();
        newNode->set(K,N,H,Ax,Ay,DI,C);
        // if first input comes, create root node and return
        if(this->root == nullptr){
            newNode->depth = 0;
            newNode->color = BLACK;
            newNode->isNew = true;
            this->root = newNode;
            return newNode;
        }
        // if root node is not empty
        Node* travel = this->root;
        Node* parent = nullptr;
        // find right position
        while(travel != nullptr){
            parent = travel;
            if(travel->number < K){
                travel = travel->right;
            }
            else{
                travel = travel->left;
            }
        }
        // set parent
        newNode->parent = parent;
        if(parent->number < K) parent->right = newNode;
        else parent->left = newNode;
        // rebalance
        if(newNode->parent->color==RED){
            fixInsert(newNode);
        }
        // return value
        return newNode;
    }

    void fixInsert(Node* node){
        // if balance needs
        while(node != nullptr && node != root && node->color==RED && (node->parent->color==RED)){
            Node* grand = node->parent->parent;
            Node* uncle = (grand->right==node->parent) ? grand->left : grand->right;
            Node* parent = node->parent;
            // case 1 => color change
            if(uncle != nullptr && uncle->color==RED){
                uncle->color =BLACK ; parent->color = BLACK;
                grand->color = RED;
                node = grand;
            }
            // case 2 => reconstruction
            else{
                // < 모양-> / 모양으로
                if((parent == grand->left) && (node == parent->right)){ // parent가 left이면서 newnode는 parent의 오른쪽
                    node = parent;
                    leftR(node); 
                }
                // > 모양 -> \ 모양으로
                else if((parent == grand->right) && (node==parent->left)){ // parent가 right이면서 newnode는 parent의 왼쪽
                    node = parent;
                    rightR(node);
                }
                // color change and rotaion \ or / -> ^
                node->parent->color = BLACK;
                grand->color = RED;
                (node == node->parent->left) ? rightR(grand) : leftR(grand);
                break;
            }
    
        }
        root->color = BLACK;
    }

    void leftR(Node* node){
        // send left of child to right of parent
        Node *tempRight = node->right;
        node->right = tempRight->left;
        if(node->right != nullptr) node->right->parent = node;
        //  grand-parent becomes child's parent
        tempRight->parent = node->parent;
        // grand-child becomes grand-parent's child
        if(tempRight->parent==nullptr) this->root = tempRight;  // change root
        else if(node->parent->left == node) node->parent->left = tempRight;
        else node->parent->right = tempRight;
        // child becomes  parent's parent
        // parent is child's child
        node->parent = tempRight;
        tempRight->left = node;
    }
    void rightR(Node* node){
        // send right of child to left of parent
        Node *tempLeft = node->left;
        node->left = tempLeft->right;
        if(node->left != nullptr) node->left->parent = node;
        //  grand-parent becomes child's parent
        tempLeft->parent = node->parent;
        // grand-child becomes grand-parent's child
        if(tempLeft->parent==nullptr) this->root = tempLeft; // change root
        else if(node->parent->left == node) node->parent->left = tempLeft;
        else node->parent->right = tempLeft;
        // child becomes  parent's parent
        // parent is child's child  
        node->parent = tempLeft;
        tempLeft->right = node;
    }


    // add Diagnosis
    Node* addIllness(int i_number, string i_illness, int i_cost){
        Node* travel = this->root;
        int deep=0;
        while(travel != nullptr){
            // if find patient
            if(travel->number == i_number){
                // add diagnosis and set depth
                travel->v_illness.push_back(i_illness);
                travel->v_cost.push_back(i_cost);
                travel->depth = deep;  
                return travel;
            }
            // if wanted patient number is greater 
            else if(travel->number < i_number){
                travel = travel->right;
                ++deep;
            }
            // if wanted patient number is less than
            else{
                travel = travel->left;
                ++deep;
            }
        }
        return nullptr; // if input number is not exist
    }
    // search
    Node* search(int s_number){
        Node* travel = this->root;
        int deep=0;
        while(travel != nullptr){
            // if find
            if(travel->number == s_number){
                travel->depth = deep; 
                travel->isNew = false; 
                return travel;
            }
            //if input number is greater
            else if(travel->number < s_number){
                travel = travel->right;
                ++deep; // add depth
            }
            //if input number is less than
            else{
                travel = travel->left;
                ++deep; //ad depth
            }
        }
        return nullptr; // if not exist 
    }
    // check epidemic size postsearch
    int epidemic(Node* node, string illness){
        int cnt = 0;
        if(node==nullptr){
            return cnt;
        }
        cnt += epidemic(node->left, illness);
        cnt += epidemic(node->right, illness);
        if(node->v_illness.back().compare(illness)==0){
            return cnt+1;
        }else{
            return cnt;
        }
    }
};





int main(int argc, char* argv[]){
    // red black tree create
    Tree* tree = new Tree();
    //variable for use
    Node* returnNode = nullptr;
    int K, Ax, Ay, C;
    string fun,N,H,DI;
    int loop=0;
    cin>>loop;

    while(loop>0){
       cin>> fun; 
       //insert
       if(fun == "I"){
           cin>>K>>N>>H>>Ax>>Ay>>DI>>C; // input
           returnNode = tree->search(K); //search if exist
           if(returnNode==nullptr){ //if new patient
               tree->insert(K,N,H,Ax,Ay,DI,C); //inesrt
               returnNode = tree->search(K); // get depth
               cout<<returnNode->depth<<" "<< 1 <<endl;
           }
           else{ // if exist
               cout<<returnNode->depth<<" "<< 0 <<endl;
           }
       }
       // find
       else if(fun =="F"){
           cin>>K;
            returnNode = tree->search(K); // check if exist
            if(returnNode==nullptr){
                cout<<"Not found"<<endl;
            }
            else{
                cout<<returnNode->depth<<" "<<returnNode->name<<" "<<returnNode->phone<<" "<<returnNode->x<<" "<<returnNode->y<<endl;
            }
       }
       // add diagnosis
       else if(fun =="A"){
           cin>>K>>DI>>C;
           returnNode = tree->addIllness(K,DI,C); // check if exist and add diagnosis
           if(returnNode==nullptr){
               cout<<"Not found"<<endl;
           }
           else{
               cout<<returnNode->depth<<endl;
           }
       }
       //check epidemic
       else if(fun =="E"){
           cin>>DI;
           int cnt = tree->epidemic(tree->root,DI); // check epidemic with illness
           cout<<cnt<<endl;
       }
       else{
           //throw out_of_range("WRONG");
       }
       loop--;
     }
    return 0;
}
