#include<iostream>
using namespace std;

int main(){
    int t;
    cin>>t;

    while(t--){
        int n;
        cin>>n;
        long long table[100001][4];
        int bi = 1000000009;
        table[0][0] = 0;
        table[1][1] = 1; table[1][2] = 0; table[2][3] = 0;
        table[2][1] = 0; table[2][2] = 1; table[2][3] = 0;
        table[3][1] = 1; table[3][2] = 1; table[3][3] = 1;
        for(int i=4; i<=n; i++){
            table[i][1] = (table[i-1][2] + table[i-1][3]) % bi;
            table[i][2] = (table[i-2][1] + table[i-2][3]) % bi;
            table[i][3] = (table[i-3][1] + table[i-3][2]) % bi;
        }
        cout<<(table[n][1]+table[n][2]+table[n][3])%bi<<endl;
    }
}
