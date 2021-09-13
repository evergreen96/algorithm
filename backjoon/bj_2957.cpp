/*
일반적인 이진검색 - 시간 초과
*/

#include <iostream>
#include <map>
#include <vector>
using namespace std;

int arr[300001] = {
    -1,
};

int main() {

  int max, num, loop = 0, count = 0, root;
  cin >> max;

  while (loop++ < max) {
    cin >> num;
    if (count == 0) {
      root = num;
      arr[num] = 0;
      cout << count << endl;
    } else {
      int i;
      if (num > root) {
        for (i = root + 1; i < num; i++) {
          if (arr[i] != -1)
            break;
        }
        arr[num] = arr[i] + 1;
        count += arr[num];
        cout << count << endl;
      } else {
        for (i = root - 1; i > 0; i--) {
          if (arr[i] != -1)
            break;
        }
        arr[num] = arr[i] + 1;
        count += arr[num];
        cout << count << endl;
      }
    }
  }
}