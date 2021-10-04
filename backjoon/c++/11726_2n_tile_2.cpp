#include<iostream>
using namespace std;

int main(){
    int t;
    cin>>t;

    while(t--){
        int n;
        cin>>n;
        int table[11];

        table[0] = 0;
        table[1] = 1;
        table[2] = 2;
        table[3] = 4;
        for(int i=4; i<=n; i++){
            table[i] = table[i-1] + table[i-2] + table[i-3];
        }
        cout<<table[n]<<endl;
    }
}
