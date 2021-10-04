#include<iostream>
using namespace std;

int main(){
    cin.tie(0);
    ios::sync_with_stdio(0);

    int n;
    cin>>n;
    long long table[10001];
    for(int i=1; i<=n; i++){
        int b;
        cin>>b;
        table[i] = b;
    }
    long long arr[10001];
    arr[1] = table[1];
    arr[2] = max(table[2], arr[1]*2);
    
    for(int i=3; i<=n; i++){
        arr[i] = table[i];
        for(int j=i-1; j >= i/2 ; j--){
            arr[i] = max(arr[i], arr[j]+arr[i-j]);
        }
    }
    cout<<arr[n]<<endl;
    
}

