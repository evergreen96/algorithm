#include <cstdio>
#include <iostream>
using namespace std;

int main() {
  freopen("input.txt", "r", stdin);
  int N;
  cin >> N;
  int* arr = new int[N];
  int* arg = new int[100](); // maximum

  int max = 0;
  for (int i = 0; i < N; i++) {
    cin >> arr[i];
    arg[arr[i]]++;
    if (max < arr[i])
      max = arr[i];
  }

  int num = 1;
  for (int i = max; i >= 0; i--) {
    if (arg[i]) {
      int j = arg[i];
      arg[i] = num;
      num += j;
    }
  }

  for (int i = 0; i < N; i++) {
    cout << arg[arr[i]] << " ";
  }

  return 0;
}