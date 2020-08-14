#include <iostream>

using namespace std;

int main() {

  int N;
  cin >> N;
  int* result = new int[N + 1]();
  int* stairs = new int[N + 1]();

  for (int i = 1; i <= N; i++) {
    cin >> stairs[i];
  }
  result[1] = stairs[1];
  result[2] = stairs[1] + stairs[2];

  for (int i = 3; i <= N; i++) {
    int output = max(stairs[i] + stairs[i - 1] + result[i - 3],
                     stairs[i] + result[i - 2]);
    result[i] = output;
  }
  cout << result[N] << endl;
}