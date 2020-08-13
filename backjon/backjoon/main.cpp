    #include <iostream>
    #include <queue>
    using namespace std;

    int x_list[4] = {-1, 0, 1, 0};
    int y_list[4] = {0, 1, 0, -1};

    struct Node {
      int x, y;
      int count = 0;
      string path = "";
    };

    void spread(string** mat, int M, int N);

    int main() {
      int M, N, X;
      cin >> M >> N >> X;

      string** mat = new string*[M];
      for (int i = 0; i < M; i++) {
        mat[i] = new string[N];
      }

      queue<Node> q;
      Node init;
      for (int i = 0; i < M; i++) {
        for (int j = 0; j < N; j++) {
          cin >> mat[i][j];
          if (mat[i][j] == "Y") {
            init = {i, j, 0};
            q.push(init);
          }
        }
      }

      Node now;
      bool flag = false;
        int s_cnt=0;
      while (!q.empty()) {
        now = q.front();
        q.pop();
        if (mat[now.x][now.y] == "E") {
          flag = true;
          break;
        }
          cout<<now.x<<" "<<now.y<<" "<<mat[now.x][now.y]<< endl;
          cout<<now.count<<endl;
          if (now.count > X && (now.count - 1) % X == 0 && (now.count-1)/X > s_cnt) {
          spread(mat, M, N);
            s_cnt++;
        }
          
        for (int i = 0; i < M; i++) {
          for (int j = 0; j < N; j++) {
            cout << mat[i][j] << " ";
          }
          cout << endl;
        }
        cout << endl;
          if(mat[now.x][now.y]=="F" || mat[now.x][now.y]=="FF")
          continue;
        int nx, ny;
        int i = 0;
        for (i; i < 4; i++) {
          nx = now.x + x_list[i];
          ny = now.y + y_list[i];
          if (0 <= nx && nx < M && 0 <= ny && ny < N) {
            if (mat[nx][ny] != "FF" && mat[nx][ny] != "F" && mat[nx][ny] != "Y" &&
                mat[nx][ny] != "V") {
                
              char dir;
              if (i == 0)
                dir = 'U';
              else if (i == 1)
                dir = 'R';
              else if (i == 2)
                dir = 'D';
              else
                dir = 'L';
              Node temp = {nx, ny, now.count + 1, now.path + dir};
              q.push(temp);
              mat[nx][ny] = 'V';
            }
          }
        }
        if (now.count >= X && (now.count) % X == 0) {
                  spread(mat, M, N);
                }
      }
      if (flag) {
        cout << now.count << "\n" << now.path << endl;
      } else {
        cout << "-1" << endl;
      }
    }

    void spread(string** mat, int M, int N) {
        for(int i=0; i<M; i++){
            for(int j=0; j<N; j++){
                if(mat[i][j]=="F"){
                     mat[i][j]="FF";
                }
            }
        }
        
      for (int i = 0; i < M; i++) {
        for (int j = 0; j < N; j++) {
          if (mat[i][j] == "FF") {
            int k = 0;
            int nx, ny;
            for (k; k < 4; k++) {
              nx = i + x_list[k];
              ny = j + y_list[k];
              if (0 <= nx && nx < M && 0 <= ny && ny < N) {
                  if(mat[nx][ny]=="FF"){
                      continue;
                  }
                if (mat[nx][ny] != "F") {
                  mat[nx][ny] = "F";
                }
              }
            }
           
          }
        }
      }
    }
