#include<iostream>
using namespace std;

int main(){
    int t;
    cin>>t;
    long long table[1001][11]={0,};
    int bi = 10007;
    
    for(int i=0; i<=9; i++){
        table[1][i] = 1;
    }

    for(int i=2; i<=t; i++){
        table[i][0] = 1;
        for(int j=1; j<=9; j++){
            table[i][j] = (table[i][j-1] + table[i-1][j])%bi;
        }
    }
    long long total = 0;
    
    for(int i=0; i<=9; i++){
        total += table[t][i];
    }
    
    cout<<total%bi<<endl;
    
    
}
