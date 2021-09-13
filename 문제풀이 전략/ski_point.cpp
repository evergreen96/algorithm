#include <iostream>
using namespace std;

//이건 내방식
int main() {
  int N;
  cin >> N;
  int** arr = new int*[N + 1];
  int** score = new int*[N + 1];
  for (int i = 0; i <= N; i++) {
    arr[i] = new int[N + 1]();
    score[i] = new int[N + 1]();
  }
  for (int i = 1; i <= N; i++) {
    for (int j = 1; j <= i; j++) {
      cin >> arr[i][j];
    }
  }
  score[1][1] = arr[1][1];
  for (int i = 2; i <= N; i++) {
    for (int j = 1; j <= i - 1; j++) {
      int bottom = score[i - 1][j] + arr[i][j];
      int right = score[i - 1][j] + arr[i][j + 1];
      score[i][j] = max(score[i][j], bottom);
      score[i][j + 1] = max(score[i][j + 1], right);
    }
  }
  int max = 0;
  for (int i = 1; i <= N; i++) {
    if (score[N][i] > max) {
      max = score[N][i];
    }
  }
  cout << max << endl;

  for (int i = 1; i <= N; i++) {
    for (int j = 1; j <= N; j++) {
      cout << score[i][j] << " ";
    }
    cout << endl;
  }
}