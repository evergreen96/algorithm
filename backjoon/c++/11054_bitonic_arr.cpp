#include<iostream>
#include<cmath>
using namespace std;


int N, K;

int arr[1001] = {0,};
int cache[1001];
int cache2[1001];
void fun(){
    for(int i = 0; i < N; i++) {
        cache[i] = 1;
        for(int j = 0; j <= i; j++) {
        
            if(arr[j] < arr[i] && cache[i] < cache[j] + 1) {
                cache[i] = cache[j] + 1;
            }
        }
    }
}

void fun2(){
    
    for(int i = N-1; i >=0; i--) {
        cache2[i] = 1;
        for(int j = N-1; j >=i; j--) {
        
            if(arr[j] < arr[i] && cache2[i] < cache2[j] + 1) {
                cache2[i] = cache2[j] + 1;
            }
        }
    }
}




int main(){
    cin>>N;
    
    for(int i=0; i<N; i++){
        cin>>arr[i];
    }
    fun(); fun2();
    int result = 0;

    
    for(int i=0; i<N; i++){
        result = max(result, cache[i]+cache2[i]-1);
    }
    
    cout<<result<<endl;

    
    
}


