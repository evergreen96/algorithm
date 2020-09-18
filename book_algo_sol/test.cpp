#include <iostream>
using namespace std;

int main() {
  int a = 3;

  if (a += 1 > 10) {
    cout << "hi";
  }
  cout << a << endl;
}