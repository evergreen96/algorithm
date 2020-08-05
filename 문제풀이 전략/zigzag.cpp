#include <iostream>
using namespace std;

int main()
{
    int maxline = 5;

    for (int i = 1; i <= maxline; i++)
    {
        if (i % 2 == 1)
        {
            for (int data = 5 * (i - 1) + 1; data <= 5 * (i - 1) + 5; data++)
            {
                cout << data << " ";
            }
            cout << endl;
        }
        else
        {
            for (int data = 5 * i; data >= (5 * i) - 4; data--)
            {
                cout << data << " ";
            }
            cout << endl;
        }
    }
}