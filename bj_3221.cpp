#include <algorithm>
#include <iostream>
using namespace std;

struct arr {
  int loc;
  char dir;
};

bool cmp(arr a, arr b) {
  if (a.loc < b.loc)
    return true;
  else
    return false;
}

int main() {
  int L, N, T;
  cin >> N >> T;
  cin >> L;
  arr* node = new arr[L];
  int num;
  char cha;
  for (int i = 0; i < L; i++) {
    cin >> num >> cha;
    node[i].loc = num;
    node[i].dir = cha;
  }

  for (int i = 0; i < L; i++) {
    if (node[i].dir == 'L') {
      node[i].loc = -node[i].loc + T;
      if (node[i].loc < 0) {
        // do not
        node[i].loc = -node[i].loc;
      } else {
        int a = node[i].loc / N;
        int b = node[i].loc % N;
        if (a % 2 == 1) {
          node[i].loc = N - b;
        } else {
          node[i].loc = b;
        }
      }
    } else {
      node[i].loc = node[i].loc + T;
      if (node[i].loc > L) {
        int a = node[i].loc / N;
        int b = node[i].loc % N;
        if (a % 2 == 1) {
          node[i].loc = N - b;
        } else {
          node[i].loc = b;
        }
      }
    }
  }
  sort(node, node + L, cmp);
  for (int i = 0; i < L; i++) {
    cout << node[i].loc << " ";
  }
}
