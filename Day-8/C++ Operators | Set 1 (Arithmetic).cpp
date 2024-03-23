#include <bits/stdc++.h>
using namespace std;

class Solution {
  public:
    vector<int> cppOperators(int A, int B) {
        // code here
        int sum = A + B;
        int product = A * B;
        int difference = (B > A) ? B - A : A - B; // Ensure positive difference
        int quotient = (B != 0) ? max(A, B) / min(A, B) : 0; // Prevent division by zero

        // Create and return the vector with the results
        return {sum, product, difference, quotient};
    }
};


int main() {
    int t;
    cin >> t;
    while (t--) {
        int A, B;
        cin >> A >> B;
        Solution ob;
        vector<int> ans = ob.cppOperators(A, B);
        for (int u : ans) cout << u << "\n";
    }
}
