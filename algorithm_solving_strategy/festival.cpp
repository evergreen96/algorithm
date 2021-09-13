#include <cstdio>
#include <iostream>
using namespace std;

int main() {
  freopen("input.txt", "r", stdin);

  int T;
  cin >> T;
  while (T--) {
    int N, B;
    cin >> N >> B;
    int* days = new int[N];
    for (int i = 0; i < N; i++) {
      cin >> days[i];
    }
    double min = 999999999.0;
    double buf = 0;
    int cnt = 1;
    for (int i = 0; i <= N - B; i++) {
      for (int j = 0; j + i < N; j++) {
        buf += days[j + i];
        if (j + 1 >= B) {
          double mid = buf / (j + 1);
          if (mid < min) {
            min = mid;
          }
        }
      }
      buf = 0;
    }
    cout.setf(ios::fixed);

    cout.precision(8);
    cout << min << endl;
  }
}