#include <cmath>
#include <iostream>
using namespace std;

int main() {
  // 2*N
  int N;
  cin >> N;
  int result;
  // 2*1 2*2
  int* arr = new int[N + 1];
  arr[0] = 0;
  arr[1] = 1;
  arr[2] = 3;
  for (int i = 3; i <= N; i++) {
    arr[i] = arr[i - 1] + arr[i - 2] * 2;
  }
}