#include <iostream>
using namespace std;

int main() {
  int N, T;
  cin >> T;
  while (T--) {
    cin >> N;
    int** arr = new int*[2];
    arr[0] = new int[N]();
    arr[1] = new int[N]();

    for (int i = 0; i < N; i++) {
      cin >> arr[0][i];
    }

    bool fin = false;
    int flag = 0;
    int i, j;
    int split = -1;

    while (!fin) {
      arr[1 - flag][N - 2] = arr[flag][N - 1];
      for (i = N - 4; i >= 0; i -= 2) {
        arr[1 - flag][i] = arr[flag][i + 1] - arr[1 - flag][i + 2];
      }
      j = i + 2;
      j = 1 - j;
      arr[1 - flag][j] = arr[flag][0] - arr[1 - flag][1 - j];

      for (i = j + 2; i < N; i += 2) {
        arr[1 - flag][i] = arr[flag][i - 1] - arr[1 - flag][i - 2];
      }
      split++;
      flag = 1 - flag;

      for (int k = 0; k < N; k++) {
        cout << arr[flag][k] << " ";
        if (arr[flag][k] < 0)
          fin = true;
      }
      cout << endl;
    }
    cout << split << endl;
  }
}
