    #include <iostream>
    using namespace std;

    int main() {
      int A, B;
      cin >> A >> B;
      int* arr = new int[A];
      for (int i = 0; i < A; i++) {
        cin >> arr[i];
      }
      int min = A + 1;
      int total = 0;
      int count = 0;
      int start = 0;
      int flag = false;
      for (int i = 0; i < A; i++) {
        total += arr[i];
        if (total < B) {
          continue;
        } else {
          flag = true;
          count = i - start + 1;
          if (min > count) {
            min = count;
          }
          while (total >= B) {
            total -= arr[start++];
            count--;
            if (total >= B) {
              if (min > count) {
                min = count;
              }
            }
          }
        }
      }
      if (!flag)
        cout << 0 << endl;
      else
        cout << min << endl;
    }
