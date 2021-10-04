#include<iostream>
using namespace std;

int table[100001] = {0,};
int cache[100001][2] = {0,};
int N;
int main(){
    cin>>N;
    
    int tmp;
    for(int i=0; i<N; i++){
        cin>>tmp;
        table[i]=cache[i][0] = cache[i][1] = tmp;
    }

    int result = cache[0][0];
    for(int i=1; i<N; i++){
        cache[i][0] = max(cache[i-1][0] + table[i], table[i]);
        cache[i][1] = max(cache[i-1][1] + table[i], cache[i-1][0]);
        
        if (result < cache[i][0]) result = cache[i][0];
        if (result < cache[i][1]) result = cache[i][1];
    }
    
    cout<<result<<endl;
    
}


