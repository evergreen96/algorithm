#include <cstdio>
#include <iostream>
using namespace std;

int** visited;
int** map;
int N;
int row_list[4] = {-1, 0, 1, 0};
int col_list[4] = {0, 1, 0, -1};

void makedong(int dong, int i, int j) {
  visited[i][j] = 1;
  map[i][j] = dong;
  int n_row;
  int n_col;
  for (int k = 0; k < 4; k++) {
    n_row = i + row_list[k];
    n_col = j + col_list[k];
    if (0 <= n_row && n_row < N && 0 <= n_col && n_col < N &&
        visited[n_row][n_col] == 0 && map[n_row][n_col] != 0) {
      makedong(dong, n_row, n_col);
    }
  }
}

int main() {
  freopen("input.txt", "r", stdin);
  int T;
  cin >> T;
  while (T--) {
    cin >> N;

    visited = new int*[N];
    map = new int*[N];

    for (int i = 0; i < N; i++) {
      visited[i] = new int[N]();
      map[i] = new int[N]();
    }

    for (int i = 0; i < N; i++) {
      for (int j = 0; j < N; j++) {
        cin >> map[i][j];
      }
    }

    int dong = 1;
    for (int i = 0; i < N; i++) {
      for (int j = 0; j < N; j++) {
        if (visited[i][j] == 0 && map[i][j] != 0) {
          makedong(dong, i, j);
          dong++;
        }
      }
    }
    cout << dong - 1 << endl;
    for (int i = 0; i < N; i++) {
      for (int j = 0; j < N; j++) {
        cout << map[i][j] << " ";
      }
      cout << endl;
    }
  }
}