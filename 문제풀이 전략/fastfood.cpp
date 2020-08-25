#include <cstdio>
#include <iostream>
using namespace std;

int main() {

  freopen("input.txt", "r", stdin);
  int N, M, P;
  cin >> N >> M >> P;
  for (int i = 0; i < P; i++) {
    int* arr = new int[N];
    for (int j = 0; j < N; j++) {
      cin >> arr[j];
    }
    int temp = M;
    for (int k = 0; k < N; k++) {
      if ((arr[k] > temp)) {
        cout << "0";
        break;
      } else {
        temp++;
        if (k == N - 1) {
          cout << "1";
        }
      }
    }
    cout << endl;
  }
  return 0;
}