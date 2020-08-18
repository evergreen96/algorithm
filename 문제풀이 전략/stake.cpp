#include <iostream>
#include <vector>
using namespace std;

int main() {
  int N;
  cin >> N;

  int* arr1 = new int[N + 1];
  int* arr2 = new int[N + 1];
  arr1[0] = arr2[0] = 0;
  for (int i = 1; i <= N; i++) {
    cin >> arr1[i] >> arr2[i];
  }

  int po;
  for (int i = 0; i < N;) {
    double max = -999;
    double ratio;
    for (int j = i + 1; j <= N; j++) {
      ratio = (double)(arr2[j] - arr2[i]) / (double)(arr1[j] - arr1[i]);

      if (ratio > max) {
        max = ratio;
        po = j;
      }
    }
    // cout<<max;
    i = po;
    cout << i << endl;
  }
}
