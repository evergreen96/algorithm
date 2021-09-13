#include<iostream>
#include<vector>
#include<queue>
#include<utility>
#include<map>
#include<unordered_map>
#define max 1000000
using namespace std;

// city info
struct City{
    string name;
    bool flooded;
    int state;
    vector<pair<int, int> > adjCity; // <adjacent city, weight>
};

// city info container
unordered_map<int, City*> vertices;

//dijkstra algorithm
void findShortestPath(char command, int start, int end){
    // exclusive case 
    if(vertices[start]->flooded == 1 || vertices[end]->flooded==1) {
        cout<<"None"<<endl;
        return;
    }
    //init - priority queue <weight - next>
    priority_queue<pair<int, int>,vector<pair<int ,int> >,greater<pair<int, int> > > pq;
    pq.push(make_pair(0, start));
    //init distance
    int *dist = new int[max];
    int *path = new int[max]; // path[A] = B means that if you want to go A you have to go B
    fill_n(path, max, 0);
    fill_n(dist, max, max+1);
    //start city init
    dist[start] = 0;
    int cnt = 0;// tree vertices count
    int cur_I; //current city int(number)
    int next_I, weight_N;
    City *cur;
    pair<int, int> p;
    int sub_shortest = 0; // shortest path of fringed city 
    while(!pq.empty()){
        sub_shortest = pq.top().first;
        cur_I= pq.top().second;  
        pq.pop();
        // if not shortest path go to next fringe city
        if(sub_shortest > dist[cur_I]) continue;
        cnt++; // tree vertices count
        if(cur_I==end) break; // if find end's shortest path
        cur = vertices[cur_I];
        int len = cur->adjCity.size();
        // update shortest path if exist
        for(int i=0; i<len; i++){
            // get adjacent city info
            p = cur->adjCity[i];
            next_I = p.first;
            weight_N = p.second;
            // if update needs
            if(dist[next_I] > dist[cur_I]+ weight_N){
                dist[next_I] = dist[cur_I] + weight_N;
                path[next_I] = cur_I;
                pq.push(make_pair(dist[next_I], next_I)); 
            }
        }
    }
    // if path is longer than max-length
    if (dist[end]> max) cout<<"None"<<endl;
    else{
        // if command is A
        if(command=='A'){
            cout<<cnt<<" "<<dist[end]<<" "<<vertices[start]->name<<" "<<vertices[end]->name<<endl;
        }
        // if command is B
        else{
            vector<int> path_V;
            path_V.clear();
            cout<<cnt<<" "; // tree vertices count
            int idx = end;
            // inverse tool of print path
            while(true){
                if(idx==start) break;
                else{
                    path_V.push_back(path[idx]);
                    idx = path[idx];
                }
            }
            // inverse print path
            while(path_V.size()!=0){
                cout<<path_V.back()<<" ";
                path_V.pop_back();
            }
            cout<<end<<endl;
        }
    }
    delete[] dist;
    delete[] path;
}


int main(){
    int n,m,q;
    cin>>n>>m>>q;
    // init vertices
    int f1;
    string f2;
    int f3;
    City *city;
    //to insert city info
    for(int i=0; i<n ;i++){
        cin>>f1>>f2>>f3;
        city = new City;
        city->name = f2;
        city->flooded = f3;
        city->state = 0;
        city->adjCity.clear();
        vertices.insert(make_pair(f1, city));
    }
    //to insert road info
    int f4,f5,f6;
    for(int i=0; i<m; i++){
        cin>>f4>>f5>>f6;
        //only when city is not flooded
        if(vertices[f4]->flooded !=1 && vertices[f5]->flooded !=1){
            vertices[f4]->adjCity.push_back(make_pair(f5, f6));
        vertices[f5]->adjCity.push_back(make_pair(f4, f6));
        }
       
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