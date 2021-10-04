#include<iostream>
using namespace std;

int table[100001] = {0,};
int cache[100001] = {0,};
int N;
int main(){
    cin>>N;
    
    int tmp;
    for(int i=0; i<N; i++){
        cin>>tmp;
        table[i]=cache[i] = tmp;
    }

    int result = cache[0];
    for(int i=1; i<N; i++){
        cache[i] = max(cache[i-1]+table[i], table[i], cache[i-1]);
        if (result < cache[i]){
            result = cache[i];
        }
    }
    
    cout<<result<<endl;
    
}


