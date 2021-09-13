#include <iostream>
using namespace std;

int main() {
  int T;
  cin >> T;
  while (T--) {
    int N;
    cin >> N;
    int* arr = new int[N];
    for (int i = 0; i < N; i++) {
      cin >> arr[i];
    }
    int max = -99999;
    int sum = 0;
    for (int i = 0; i < N; i++) {
      sum += arr[i];
      if (sum > max)
        max = sum;
    }
    if (sum < 0)
      sum = 0;
  }
}