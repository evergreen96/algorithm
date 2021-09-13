#include <iostream>
using namespace std;

int main() {
  int N;
  cin >> N;
  int days_price[11] = {0, 12, 21, 31, 40, 49, 58, 69, 79, 90, 101};
  int* minimum = new int[N + 1]();
  for (int i = 1; i <= N; i++) {
    minimum[i] = days_price[1] * (i);
  }
  for (int i = 2; i <= 10; i++) {
    int new_price = days_price[i];
    if (minimum[i] > new_price) {
      minimum[i] = new_price;
    }
    for (int j = i + 1; j <= N; j++) {
      if (minimum[j] > new_price + minimum[j - i]) {
        minimum[j] = new_price + minimum[j - i];
      }
    }
  }
  cout << minimum[N] << endl;
}