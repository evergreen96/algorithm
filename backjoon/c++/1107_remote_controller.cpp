#include<iostream>
#include<cmath>
#include<string>
using namespace std;



int N, M;
int arr[10]={0,};

bool check(int num){
    string str = to_string(num);
    
    for(int i=0; i<str.length(); i++){
        if(arr[str[i]-'0']==1){
            return false;
        }
    }
    return true;
}

int main(){
    
    
    cin>>N>>M;
    unsigned long tmp = 0;
    for(int i=0; i<M; i++){
        cin>>tmp;
        arr[tmp] = 1;
    }
    unsigned long result = abs(N-100);
    
    for(int i=0; i<=1000000; i++){
        if(check(i)){
            string str = to_string(i);
            tmp = str.length();
            tmp += abs(N-i);
            result = min(result, tmp);

        }
    }
    
    cout<<result<<endl;
}


