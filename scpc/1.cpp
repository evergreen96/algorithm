
#include <iostream>
#define fio                                                                    \
  ios::sync_with_stdio(false);                                                 \
  cin.tie(0);                                                                  \
  cout.tie(0);
using namespace std;
typedef long long int ll;
typedef long double ldb;
// mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());
const bool debug = false;
const int mod = 998244353;

ll a[222222], b[222222], n, k, ans;

void solve(void) {
  int i;
  cin >> n >> k;
  ans = 0;
  for (i = 1; i <= n; i++)
    cin >> a[i];
  sort(a + 1, a + n + 1);
  for (i = 1; i <= n; i++)
    cin >> b[i];
  sort(b + 1, b + n + 1);
  for (i = 1; i <= k; i++)
    ans = max(ans, a[i] + b[k + 1 - i]);
  cout << ans;
}

int main(void) {
  fio;
  int tc;
  cin >> tc;
  for (int i = 1; i <= tc; i++) {
    cout << "Case #" << i << "\n";
    solve();
    cout << "\n";
  }
  return 0;
}
