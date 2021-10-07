#include<iostream>
#include<cmath>
#include<string>
using namespace std;



int N, M;
int main(){
    cin>>N;
    if (N<=9) cout<<N<<endl;
    else{
        int v = 9, i = 1;
        int result = 0;
        while(v <= N){
            result += i*v;
            N -= v;
            v *=10;
            i++;
        }
        result += N*i;
        cout<<result<<endl;
    }
}


