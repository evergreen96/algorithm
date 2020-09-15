#include <iostream>
using namespace std;

int main() {
  int N;
  cin >> N;
  int* arr = new int[N + 1];
  arr[0] = 1;
  arr[1] = 0;
  arr[2] = 3;
  arr[4] = 11;
  for (int i = 6; i <= N; i += 2) {
    arr[i] = (arr[i - 2] * 3);
    for (int j = i - 4; j >= 0; j -= 2) {
      arr[i] += arr[j] * 2;
    }
  }
  cout << arr[N] << endl;
}