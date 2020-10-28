#include <cstdio>
#include <iostream>
#include <vector>
using namespace std;
// n이 커지면 시간초과

int main(){
    
    int a=1;
    int b=2;
    if((a +=1) <1)
        cout<<"a"<<endl;
    if( b +=1 < 1)
        cout<<"b"<<endl;
    cout<<a<<b<<endl;
}
