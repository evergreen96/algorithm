#include <cstdio>
#include <iostream>
using namespace std;

const char connected_list[10][17] = {"1110000000000000", "0001000101010000",
                                     "0000100000100011", "1000111100000000",
                                     "0000001110101000", "1010000000000011",
                                     "0001000000000011", "0000110100000011",
                                     "0111110000000000", "0001110001000100"};

int minv = 987654321;
bool check(int* numbers) {
  for (int i = 0; i < 16; i++) {
    if (numbers[i] != 12)
      return false;
  }
  return true;
}

void circle(int* numbers, int pos) {
  for (int i = 0; i <= 15; i++) {
    if (connected_list[pos][i] == '1')
      numbers[i] += 3;
    if (numbers[i] > 12)
      numbers[i] = 3;
  }
}

int cal(int* numbers, int pos, int cnt) {

  if (check(numbers)) {
    return min(cnt, minv);
  }
  if (pos > 9) {
    return minv;
  }
  int ret;
  for (int j = 0; j < 4; j++) {
    int buf = cal(numbers, pos + 1, cnt + j);
    circle(numbers, pos);
    ret = minv = min(buf, minv);
  }
  return ret;
}

int main() {
  freopen("input.txt", "r", stdin);
  int T;
  cin >> T;

  while (T--) {
    minv = 987654321;
    int numbers[16];
    for (int i = 0; i < 16; i++) {
      cin >> numbers[i];
    }

    int result = cal(numbers, 0, 0);
    if (result == 987654321)
      cout << -1 << endl;
    else {
      cout << result << endl;
    }
  }
}