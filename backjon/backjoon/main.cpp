/*
일반적인 이진검색 - 시간 초과
*/

#include <iostream>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

int arr[300001]={0,};



int main() {
  int max, num, loop = 0, count = 0, root;
  cin >> max;

  while (loop++ < max) {
    cin >> num;
    if (loop == 1) {
      root = num;
      arr[num] = 0;
      cout << count << endl;
    } else {
      int i;
      if (num > root) {
        for (i = num-1; i > root; i--) {
          if (arr[i] != 0)
            break;
        }
        arr[num] = arr[i] + 1;
        count += arr[num];
        cout << count << endl;
      } else {
        for (i = num+1; i <root; i++) {
          if (arr[i] != 0)
            break;
        }
        arr[num] = arr[i] + 1;
        count += arr[num];
        cout << count << endl;
      }
    }
  }
}
