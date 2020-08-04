
#include <iostream>
using namespace std;
int main(int argc, const char * argv[]) {
    
    int a;
    cin>>a;
    int count=0;
    while(a > 0){
        if(a>=5){
            a -=5;
            count++;
        }else if( a>=3){
            a -=3;
            count++;
        }else{
            break;
        }
    }
    if(a==0) cout<<count<<endl;
    else cout<<-1<<endl;
    return 0;
}
