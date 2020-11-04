#include <iostream>
#include <vector>
using namespace std;
void normalize(vector<int> &num);
// 입력된 수들이 a,b에 역으로 정렬 - 계산용이
vector<int> multiply(vector<int> &a, vector<int> &b);
int main()
{
    return 0;
}

void normalzie(vector<int> &num)
{
    num.push_back(0);
    //자릿수 올림
    for (int i = 0; i + 1 < num.size(); i++)
    {
        if (num[i] < 0)
        {
            int borrow = (abs(num[i]) + 9) / 10;
            num[i + 1] -= borrow;
            num[i] += borrow * 10;
        }
        else
        {
            num[i + 1] += num[i] / 10;
            num[i] %= 10;
        }
    }
    while (num.size() > 1 & num.back() == 0)
        num.pop_back();
}

// 입력된 수들이 a,b에 역으로 정렬 - 계산용이
vector<int> multiply(vector<int> &a, vector<int> &b)
{
    vector<int> c(a.size() + b.size() + 1, 0);

    for (int i = 0; i < a.size(); i++)
    {
        for (int j = 0; j < b.size(); j++)
        {
            c[i + j] += a[i] * b[i];
        }
    }
    // normalize(c);
    return c;
}
