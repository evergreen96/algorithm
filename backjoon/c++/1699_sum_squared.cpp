#include<iostream>
#include<cmath>
using namespace std;


int N;
int main(){
    cin>>N;
    
    int arr[100001] = {0,};
    arr[1] = 1;
    arr[2] = 2;
    arr[3] = 3;
    arr[4] = 1;
    for(int i=5; i<=N; i++){
        arr[i] = i;
        
        for(int j=1; j*j<=i; j++){
            arr[i] = min(arr[i], arr[i-j*j]+1);
        }
     
    }
    cout<<arr[N]<<endl;
}


