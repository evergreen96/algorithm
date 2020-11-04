#include <cstdio>
#include <iostream>
using namespace std;

int jjack[10][10];

int cal(int* stu, int N) {
  int ff = -1;
  for (int i = 0; i < N; i++) {
    if (stu[i] == 0) {
      ff = i;
      break;
    }
  }

  if (ff == -1)
    return 1;
  int ret = 0;

  for (int i = ff + 1; i < N; i++) {
    if (stu[i] == 0 && jjack[ff][i] == 1) {
      stu[i] = stu[ff] = 1;
      ret += cal(stu, N);
      stu[i] = stu[ff] = 0;
    }
  }
  return ret;
}

int main() {

  freopen("input.txt", "r", stdin);
  int T;
  cin >> T;
  while (T--) {
    int N, M;
    cin >> N >> M;
    int* stu = new int[N]();

    for (int i = 0; i < 10; i++) {
      for (int j = 0; j < 10; j++) {
        jjack[i][j] = 0;
      }
    }

    int a, b;
    for (int i = 0; i < M; i++) {
      cin >> a >> b;
      jjack[a][b] = 1;
    }

    int result = cal(stu, N);
    cout << result << endl;
  }
}