#include <iostream>
using namespace std;

int main()
{
    int num;
    cin >> std::hex >> num;
    cout << num << endl;

    cin >> std::dec >> num;
    cout << std::hex << num << endl;
}