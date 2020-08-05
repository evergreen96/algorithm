#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    int number;
    number = rand() % 100;
    int guess;
    int i = 1;
    while (true)
    {
        cout << i << " guess the number : ";
        cin >> guess;
        i++;
        if (guess == number)
        {
            cout << "Correct" << endl;
            break;
        }
        else if (guess < number)
        {
            cout << "bigger than yours" << endl;
        }
        else
        {
            cout << "smaller than yours" << endl;
        }
    }
}