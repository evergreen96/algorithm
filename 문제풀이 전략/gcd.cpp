#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    int data1, data2;
    cin >> data1 >> data2;

    int gcd = 1;
    int min = (data1 > data2) ? data2 : data1;

    for (int i = 1; i <= min; i++)
    {
        if ((data1 % i) == 0 && (data2 % i) == 0)
        {
            gcd = i;
        }
        if (i == data1 || i == data2)
        {
            break;
        }
    }
    cout << gcd << endl;

    return 0;
}