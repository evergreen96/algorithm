#include<iostream>
#include<cmath>
#include<string>
using namespace std;



int N, M;
int main(){
    cin>>N;
    
    while(N--){
        int a,b,c,d;
        cin>>a>>b>>c>>d;
        
        long long result = c;
        int start = c, end = c;
        bool flag = false;
        int w = a>b ? a : b;
        for(int i=0; i<w; i++){
            while (end>b) end -= b;
            while (end <=0)end +=b;
            
            if(end==d){
                flag= true;
                break;
            }
            
            end += a;
            result += a;
        }
        if(flag) cout<<result<<endl;
        else cout<<-1<<endl;
        
        
        
    }
}


