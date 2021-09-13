#include <iostream>
#include <string>
#include <vector>
using namespace std;

string ra(string::iterator &it)
{
    char head = *it;
    ++it;
    if (head == 'b' || head == 'w')
        return string(1, head);
    string ul = ra(it);
    string ur = ra(it);
    string ll = ra(it);
    string lr = ra(it);

    return string("x") + ll + lr + ul + ur;
}

string ra2(string it, int &num)
{
    char head = it[num];
    num++;
    string re(1, head);
    if (head == 'b' || head == 'w')
        return re;
    string ul = ra2(it, num);
    string ur = ra2(it, num);
    string ll = ra2(it, num);
    string lr = ra2(it, num);

    return string("x") + ll + lr + ul + ur;
}

int main()
{
    int T;
    cin >> T;

    while (T--)
    {
        /*
       vector<string> tree;
        string buf;
        cin>>buf;
        tree.push_back(buf);
        cout<<ra(tree.begin())<<endl;
         */
        string tree;
        int num = 0;
        cin >> tree;
        cout << ra2(tree, num) << endl;
    }
}
