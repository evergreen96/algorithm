#include<iostream>
#include<cmath>
using namespace std;


int N, K;
int main(){
    cin>>N>>K;
    
    long long arr[201][201] = {0,};
    int di = 1000000000;
    
    for(int i=0; i<=N;i++){
        arr[i][1] = 1;
        //arr[1][i] = i;
        //arr[0][i] = 1;
    }
    
    for(int i=2; i<=K; i++){
        for(int j=0; j<=N; j++){
            for(int t=0; t<=j; t++){
                arr[j][i] = (arr[j][i] + arr[t][i-1]) %di;
            }
        }
    }
    
    
    cout<<arr[N][K]<<endl;
}


