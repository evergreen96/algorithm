#include<algorithm>
#include<iostream>
#include<cstring>
using namespace std;

/*
1
12341234 


5 
12341234 
11111222 
12122222 
22222222 
12673939
*/

string ss;
int cache[10002];

int score(string m);

int mesmerize(int idx){
    if (idx==ss.length()) return 0;

    int& ret = cache[idx];
    if(ret != -1) return ret;

    ret = 1000000000;

    for(int next=3; next<6; next++){
        if (idx+next <= ss.length()){
            ret = min(ret, mesmerize(idx+next)+score(ss.substr(idx, next)));
        }
    }
    return ret;
}

int score(string m){
    // 난이도 1 검사 - 모두 같은 수 
	if(m == string(m.size(), m[0])) return 1;
	
	// 난이도 2 검사 - 등차수열이자 공차가 1 or -1 
	bool prog = true;
	for(int i=0;i<m.size()-1;i++) 
		if(m[i+1] - m[i] != m[1] - m[0]) prog = false;
		
	if(prog && abs(m[1] - m[0]) == 1) return 2;
	
	// 난이도 4 검사 - 두 수 번갈아가면서
	bool alter =  true;
	for(int i=0;i<m.size();i++) 
		if(m[i] != m[i%2]) alter = false;
	
	if(alter) return 4;
	
	// 난이도 5 검사 - 등차수열
	if(prog) return 5;
	
	// 이외 
	return 10;
}


int main(){
    	// cin.tie(NULL);
	ios::sync_with_stdio(false);
    int N;
    cin>>N;
    while(N--){
    cin>>ss;
       memset(cache, -1, sizeof(cache));
    cout<<mesmerize(0)<<endl;
    }
}