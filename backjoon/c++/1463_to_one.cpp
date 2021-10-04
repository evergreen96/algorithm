#include<iostream>
using namespace std;



int main(){
    int n;
    cin>>n;
    int arr[10000001];
    arr[0] = arr[1] = 0;
    arr[2] = arr[3] = 1;

    if(n<=3){
        cout<<arr[n]<<endl;
    }
    else{
        for(int i=4; i<=n; i++){
            int a = i%3==0 ? arr[i/3] : 100000000;
            int b = i%2==0 ? arr[i/2]: 100000000;
            int c = arr[i-1];
            arr[i] = min(min(a, b), c) + 1;
        }
        cout<<arr[n]<<endl;
    }
}