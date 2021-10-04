#include<iostream>
using namespace std;

int table[10001] = {0,};
int dp[10001] = {0,};
int main(){
    int t;
    cin>>t;
    
    for(int i=1; i<=t; i++){
        cin>>table[i];
    }
    
    dp[0] = 0;
    dp[1] = table[1];
    dp[2] = table[1] + table[2];
    
    for(int i=3; i<=t; i++){
        int a = dp[i-2] + table[i];
        int b = dp[i-3] + table[i-1] + table[i];
        int c = dp[i-1];
        
        dp[i] = max(max(a,b), c);
    }
    
    cout<<dp[t]<<endl;
}


