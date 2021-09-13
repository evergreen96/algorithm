#include <iostream>
using namespace std;

int main()
{
    int n, n1 = 0, n2 = 1;
    int loop;
    cin >> loop;
    for (int i = 1; i <= loop; i++)
    {
        n = n1 + n2;
        cout << n << " ";
        if (i % 10 == 0)
            cout << "\n";
        n1 = n2;
        n2 = n;
    }
}