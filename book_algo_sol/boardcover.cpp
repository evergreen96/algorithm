#include <cstdio>
#include <iostream>
using namespace std;

int map[20][20];

const int coverType[4][3][2] = {{{0, 0}, {1, 0}, {0, 1}},
                                {{0, 0}, {1, 0}, {1, 1}},
                                {{0, 0}, {0, 1}, {1, 1}},
                                {{0, 0}, {1, 0}, {1, -1}}};

bool set(int H, int W, int y, int x, int type, int back) {
  bool ok = true;
  for (int i = 0; i < 3; i++) {
    int ny = y + coverType[type][i][0];
    int nx = x + coverType[type][i][1];
    if (ny < 0 || ny >= H || nx < 0 || nx >= W)
      ok = false;
    else if ((map[ny][nx] += back) < 0)
      ok = false;
  }
  return ok;
}

int cal(int H, int W) {

  int y = -1, x = -1;
  for (int i = 0; i < H; i++) {
    for (int j = 0; j < W; j++) {
      if (map[i][j] == 1) {
        y = i;
        x = j;
        break;
      }
    }
    if (y != -1)
      break;
  }

  if (y == -1)
    return 1;
  int ret = 0;
  for (int i = 0; i < 4; i++) {
    if (set(H, W, y, x, i, -1))
      ret += cal(H, W);
    set(H, W, y, x, i, 1);
  }
  return ret;
}

int main() {
  freopen("input.txt", "r", stdin);
  int T;
  cin >> T;
  while (T--) {
    int H, W;
    cin >> H >> W;

    char temp;
    for (int i = 0; i < H; i++) {
      for (int j = 0; j < W; j++) {
        cin >> temp;
        if (temp == '#')
          map[i][j] = 0;
        else {
          map[i][j] = 1;
        }
      }
    }

    int result = cal(H, W);
    cout << result << endl;
  }
}