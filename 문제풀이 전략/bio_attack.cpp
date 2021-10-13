#include <cstdio>
#include <iostream>
#include <queue>
using namespace std;

int main() {
  freopen("input.txt", "r", stdin);
  int N, M;
  cin >> M >> N;
  int human_cnt = 0;
  int** human = new int*[N];
  int** visited = new int*[N];

  for (int i = 0; i < N; i++) {
    human[i] = new int[M];
    visited[i] = new int[M]();
  }

  for (int i = 0; i < N; i++) {
    for (int j = 0; j < M; j++) {
      cin >> human[i][j];
      if (human[i][j] == 1)
        human_cnt++;
    }
  }
  queue<pair<int, int> > q;
  int a, b;
  cin >> a >> b;
  visited[a - 1][b - 1] = 1;
  q.push(make_pair(a - 1, b - 1));
  int row_list[4] = {-1, 0, 1, 0};
  int col_list[4] = {0, 1, 0, -1};
  int row, col, depth;
  int days = 0;

  while (!q.empty()) {
    row = q.front().first;
    col = q.front().second;
    q.pop();
    depth = visited[row][col];

    for (int i = 0; i < 4; i++) {
      int n_row = row + row_list[i];
      int n_col = col + col_list[i];
      if (0 <= n_row && n_row < N && 0 <= n_col && n_col < M &&
          visited[n_row][n_col] == 0 && human[n_row][n_col] != 0) {
        if (human[n_row][n_col] != 0) {
          human_cnt--;
          days = depth + 1;
          visited[n_row][n_col] = depth + 1;
        }
        if (human_cnt == 0)
          break;
        q.push(make_pair(n_row, n_col));
      }
    }

    if (human_cnt == 0)
      break;
  }
  cout << days << endl;
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < M; j++) {
      cout << visited[i][j] << " ";
    }
    cout << endl;
  }
}
