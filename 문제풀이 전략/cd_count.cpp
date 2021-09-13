#include <iostream>
using namespace std;

int main()
{
    cout << " 1~1000" << endl;
    int num, count = 0, total = 0;
    cin >> num;
    for (int i = 1; i <= 1000; i++)
    {
        if (i % num == 0)
        {
            total += i;
            count++;
        }
    }
    cout << total << " " << count << endl;
}