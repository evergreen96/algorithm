#include <iostream>
using namespace std;

int gcd(int a, int b)
{
    if (b != 0)
    {
        cout << a << " " << b << endl;
        return gcd(b, a % b);
    }
    else
    {
        return a;
    }
}

int main()
{
    int a, b;
    cin >> a >> b;
    int g = gcd(a, b);
    cout << g << endl;
}