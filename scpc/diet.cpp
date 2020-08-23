/*
You should use the standard input/output

in order to receive a score properly.

Do not use file input and output

Please be very careful.
*/
#include <algorithm>
#include <cstdio>
#include <iostream>
using namespace std;

int Answer;

int main(int argc, char** argv) {
  std::ios_base::sync_with_stdio(false);
  int T, test_case;
  /*
     The freopen function below opens input.txt file in read only mode, and
     afterward, the program will read from input.txt file instead of
     standard(keyboard) input. To test your program, you may save input data in
     input.txt file, and use freopen function to read from the file when using
     cin function. You may remove the comment symbols(//) in the below statement
     and use it. Use #include<cstdio> or #include <stdio.h> to use the function
     in your program. But before submission, you must remove the freopen
     function or rewrite comment symbols(//).
   */

  // freopen("input.txt", "r", stdin);

  cin >> T;
  for (test_case = 0; test_case < T; test_case++) {

    Answer = 0;
    int N, K;
    cin >> N >> K;

    int* A = new int[N];
    int* B = new int[N];

    for (int i = 0; i < N; i++) {
      cin >> A[i];
    }

    for (int i = 0; i < N; i++) {
      cin >> B[i];
    }
    sort(A, A + N);
    sort(B, B + N);
    Answer = max(A[0] + B[K - 1], B[0] + A[K - 1]);

    // Print the answer to standard output(screen).
    cout << "Case #" << test_case + 1 << endl;
    cout << Answer << endl;
  }

  return 0; // Your program should return 0 on normal termination.
}

/*

 5
 2 2
 1 2
 4 2
 3 2
 1 3 6
 1 3 4
 5 2
 1 2 3 4 5
 6 7 8 9 10
 5 3
 3 6 2 9 12
 7 4 2 3 9
 4 3
 1 8 6 5
 2 3 5 7
 Case #1
 5
 Case #2
 4
 Case #3
 8
 Case #4
 8
 Case #5
 8
 */
