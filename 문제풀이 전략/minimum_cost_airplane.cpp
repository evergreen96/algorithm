#include <cstdio>
#include <iostream>
using namespace std;

int fare = 0;
int finalfare = 9999;
bool* visited;
int** arr;
int cnt = 0;
int N;
void travel(int loc) {
  visited[loc] = true;
  cnt++;

  if (cnt == 5 && arr[loc][0] != 0) {
    if (finalfare > fare + arr[loc][0]) {
      finalfare = fare + arr[loc][0];
    }
    cnt--;
    visited[loc] = false;

    return;
  }

  for (int i = 1; i < N; i++) {
    if (visited[i] != true && arr[loc][i] != 0) {
      if (finalfare < fare + arr[loc][i]) {
        continue;
      }
      fare = fare + arr[loc][i];
      travel(i);
      fare = fare - arr[loc][i];
    }
  }

  visited[loc] = false;
  cnt--;

  return;
};

int main() {
  freopen("input.txt", "r", stdin);
  int T;
  cin >> T;
  while (T--) {
    cin >> N;
    arr = new int*[N];
    for (int i = 0; i < N; i++) {
      arr[i] = new int[N]();
    }

    for (int i = 0; i < N; i++) {
      for (int j = 0; j < N; j++) {
        cin >> arr[i][j];
      }
    }

    visited = new bool[N]();

    travel(0);

    cout << finalfare << endl;
  }
}