#include <iostream>
#include <algorithm>
using namespace std;

int *arr;

void qsort(int start, int end)
{
    if (start <= end)
    {
        int left, right, pivot;
        pivot = arr[(start + end) / 2];
        left = start;
        right = end;
        while (left <= right)
        {
            while (arr[left] < pivot)
                left++;
            while (arr[right] > pivot)
                right--;
            if (left <= right)
            {
                swap(arr[left], arr[right]);
                left++;
                right--;
            }
        }
        qsort(start, right);
        qsort(left, end);
    }
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int n;
    cin >> n;
    arr = new int[n];

    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }

    qsort(0, n - 1);

    for (int i = 0; i < n; i++)
    {
        cout << arr[i] << "\n";
    }
}
