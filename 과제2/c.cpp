#include<iostream>
#include<vector>
#include<queue>
#include<utility>
#include<map>
#include<unordered_map>
#define max 1000000
using namespace std;


struct City{
    string name;
    bool flooded;
    vector<pair<int, int> > adjCity; // <adjacent city, weight>
};

unordered_map<int, City*> vertices;

void findShortestPath(char command, int start, int end){
    // exclusive case 
    if(vertices[start]->flooded == 1 || vertices[end]->flooded==1) {
        cout<<"None"<<endl;
        return;
    }
    //init
    priority_queue<pair<int,int> > pq; //weight - next
    pq.push(make_pair(0, start));
    //init distance
    int *dist = new int[max];
    int *visit = new int[max];
    int *path = new int[max]; // path[A] = B means that if you want to go A you have to go B
    fill_n(path, max, 0);
    fill_n(visit, max, 0);
    fill_n(dist, max, max+1);
    dist[start] = 0;
    int cnt = 0;// tree vertices count
    int cur_I; //current city number
    int next_I, weight_N;
    City *cur, *next;
    pair<int, int> p;
    while(!pq.empty()){
        cur_I= pq.top().second;  
        pq.pop();
        if(visit[cur_I]==1) continue; 
        visit[cur_I] = 1;
        cnt++;
        if(cur_I == end) break; // find shortest path
        cur = vertices[cur_I];
        int len = cur->adjCity.size();
        // update shortest path if exist
        for(int i=0; i<len; i++){
            // get adjacent city info
            p = cur->adjCity[i];
            next_I = p.first;
            weight_N = p.second;
            next = vertices[next_I];
            if(next->flooded == 1) continue;
            // if update needs
            if(dist[next_I] > dist[cur_I]+ weight_N){
                dist[next_I] = dist[cur_I] + weight_N;
                path[next_I] = cur_I;
                pq.push(make_pair(-dist[next_I], next_I)); 
            }
            else if(dist[next_I]== dist[cur_I]+ weight_N){
                if(path[next_I] > cur_I) path[next_I] = cur_I;
            }
        }
    }

    if (dist[end]> max) cout<<"None"<<endl;
    else{
        if(command=='A'){
            cout<<cnt<<" "<<dist[end]<<" "<<vertices[start]->name<<" "<<vertices[end]->name<<endl;
        }else{
            vector<int> path_V;
            path_V.clear();
            cout<<cnt<<" ";
            int idx = end;
            while(true){
                if(path[idx]==0) break;
                else{
                    path_V.push_back(path[idx]);
                    idx = path[idx];
                }
            }
            while(path_V.size()!=0){
                cout<<path_V.back()<<" ";
                path_V.pop_back();
            }
            cout<<end<<endl;
        }
    }
    delete[] dist;
    delete[] path;
    delete[] visit;
}


int main(){
    freopen("input.in","r", stdin);

    int n,m,q;
    cin>>n>>m>>q;
    // init vertices
    int f1;
    string f2;
    int f3;
    City *city;
    for(int i=0; i<n ;i++){
        cin>>f1>>f2>>f3;
        city = new City;
        city->name = f2;
        city->flooded = f3;
        city->adjCity.clear();
        vertices.insert(make_pair(f1, city));
    }
    //init edges
    int f4,f5,f6;
    for(int i=0; i<m; i++){
        cin>>f4>>f5>>f6;
        vertices[f4]->adjCity.push_back(make_pair(f5, f6));
        vertices[f5]->adjCity.push_back(make_pair(f4, f6));
    }


    // question
    char AorB;
    int start, end;
    while(q){
        cin>>AorB>>start>>end;
        findShortestPath(AorB, start, end);
        q--;
    }
}