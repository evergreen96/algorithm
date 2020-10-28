#include <cstdio>
#include <iostream>
#include <vector>
using namespace std;
// n이 커지면 시간초과
// 2 5 4 0 7 1 6 3
double cities[8][8];
bool visited[8];
vector<int> v;
vector<double> m;

vector<double> m2;
void visited_reset() {
  for (int i = 0; i < 8; i++) {
    visited[i] = false;
  }
}

void cities_reset() {
  for (int i = 0; i < 8; i++) {
    for (int j = 0; j < 8; j++) {
      cities[i][j] = 0;
    }
  }
}
int cnt = 0;
double cal(int N, int ptr, double _len) {
  cnt++;
  int index = -1;
  double len = 10000000000000;

  for (int i = 0; i < N; i++) {
    if (visited[i] == false) {
      index = i;
      break;
    }
  }
  if (index == -1)
    return _len;

  for (int i = 0; i < N; i++) {
    if (visited[i] == true)
      continue;
    //_len += cities[ptr][i];
    // as;ldfkjasdfl;ksjfasl;dkfjdsal;kfjasl;kfjdasfl;kdajsfl;kasjfl;k 이런 실수

    visited[i] = true;

    v.push_back(i);
    m.push_back(cities[ptr][i]);
    m2.push_back(_len);
    double temp = cal(N, i, _len + cities[ptr][i]);
    len = min(len, temp);
    visited[i] = false;
    v.pop_back();
    m.pop_back();
    m2.pop_back();
  }
  return len;
}

int main() {
  freopen("input.txt", "r", stdin);
  int T;
  cin >> T;
  while (T--) {
    int N;
    cin >> N;
    cities_reset();
    visited_reset();

    for (int i = 0; i < N; i++) {
      for (int j = 0; j < N; j++) {
        cin >> cities[i][j];
      }
    }

    double result = 1000000000000;
    for (int i = 0; i < N; i++) {
      visited[i] = true;
      v.push_back(i);
      m.push_back(0);
      m2.push_back(0);
      result = min(result, cal(N, i, 0.0));
      visited_reset();
      v.pop_back();
      m.pop_back();
      m2.pop_back();
    }
    cout.precision(12);
    cout << result << endl;
  }
}