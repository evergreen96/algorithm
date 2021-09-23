#include<algorithm>
#include<iostream>
using namespace std;



int a,b;
int cache[101][101];
int ta[100];
int tb[100];


int j_lis(int idx_a, int idx_b){
    
    int& cnt = cache[idx_a+1][idx_b+1];
    if (cnt != -1) return cnt;
    const long long NEGINF = numeric_limits<long long>::min();
    cnt = 2;
    long long aa = (idx_a==-1) ? NEGINF : ta[idx_a];
    long long bb = (idx_b==-1) ? NEGINF : tb[idx_b];
    long long maxV = max(aa, bb);

    for(int next_a=idx_a+1; next_a<a; next_a++){
        if (maxV< ta[next_a]){
            cnt = max(cnt, j_lis(next_a, idx_b)+1);
        }
    }
        for(int next_b=idx_b+1; next_b<b; next_b++){
        if (maxV< tb[next_b]){
            cnt = max(cnt, j_lis(idx_a, next_b)+1);
        }
    }

    return cnt;
}

void solution();


int main(){
    int N;
    cin>>N;
    for(int i=0; i<N; i++){
        solution();
    }
    return 0;
}




void solution(){
    cin>>a>>b;
    for(int i=0; i<a; i++){
        cin>>ta[i];
    }
        for(int i=0; i<b; i++){
        cin>>tb[i];
    }

    for(int i=0; i<101; i++){
        for (int j=0; j<101; j++){
            cache[i][j] = -1;
        }
    }
    cout<<j_lis(-1,-1)-2<<endl;
}

/*

1
5 3
10 20 30 1 2
10 20 30

3
3 3
1 2 4
3 4 7
3 3
1 2 3
4 5 6
5 3
10 20 30 1 2
10 20 30
*/