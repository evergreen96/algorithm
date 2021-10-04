    #include<iostream>
    using namespace std;
    long long arr[100001][2] = {0,};
    long long dp[100001][2] = {0,};

    int main(){
        int t;
        cin>>t;
        
        while(t--){
            int n;
            cin>>n;
            
            int a;
            for(int i=0; i<n; i++){
                cin>>a;
                arr[i][0] = a;
            }
            for(int i=0; i<n; i++){
                cin>>a;;
                arr[i][1] = a;
            }
            
            if (n == 1){
                cout<<max(arr[0][0], arr[1][0])<<endl;
                return 0;
            }
            
            dp[0][0] = arr[0][0];
            dp[0][1] = arr[0][1];
            dp[1][0] = arr[1][0] + arr[0][1];
            dp[1][1] = arr[0][0] + arr[1][1];
            
            for(int i=2; i<n; i++){
                dp[i][0] = arr[i][0] + max(dp[i-1][1], dp[i-2][1]);
                dp[i][1] = arr[i][1] + max(dp[i-1][0], dp[i-2][0]);
            }
            
            cout<<max(dp[n-1][0], dp[n-1][1])<<endl;
            
        }
        
    }


