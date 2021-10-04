#include<iostream>
using namespace std;

int main(){
    cin.tie(0);
    ios::sync_with_stdio(0);

    int t;
    cin>>t;
    
    long long table[1000009];
    //1,000,000,009
    int di = 1000000009;
    
    table[1] = 1;
    table[2] = 2;
    table[3] = 4;
    for(int i=4; i<=1000000; i++){
        table[i] = (table[i-1] +  table[i-2] +  table[i-3]) % di;
    }
    int n;
    while(t--){
        cin>>n;
        cout<<table[n]<<'\n';
    }
}

