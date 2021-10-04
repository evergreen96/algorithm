#include<iostream>
using namespace std;

int table[1001] = {0,};
int cache[1001] = {0,};
int route[1001] = {0,};
int N;
int LIS(int);
int main(){
    cin>>N;
    for(int i=1; i<=N; i++){
        cin>>table[i];
    }
    cout<<LIS(0)<<endl;

    
}


int LIS(int now){
    int& ret = cache[now];
    if(ret != 0) return ret;
    
    ret = table[now];
    for(int next=now+1; next<=N; next++){
        if( now==0 | table[next]> table[now]){
            ret = max(ret, LIS(next)+table[now]);
        }
    }
    return ret;
}



