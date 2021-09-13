#include <cstdio>
#include <iostream>
using namespace std;

int main() {
  freopen("input.txt", "r", stdin);
  int T;
  cin >> T;
  while (T--) {
    string input;
    cin >> input;
    int len = input.length();
    bool flag = false;
    for (int i = 1; i < len; i++) {
      for (int j = 0; j + i < len; j++) {
        int k = i; //반복이 되는지 안되는지 길이만큼 확인해야 한다.
        while (k--) {
          if (input[j] == input[j + i]) {
            flag = true;
          } else {
            flag = false;
            break;
          }
          j++;
        }
        if (flag == true) {
          break;
        }
      }
      if (flag == true) {
        break;
      }
    }
    if (flag) {
      cout << "dont" << endl;
    } else {
      cout << "can" << endl;
    }
  }
}