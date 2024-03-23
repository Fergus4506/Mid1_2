#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
    while (1) {
        int n;
        cin >> n;
        if (n == 0) {
            break;
        }
        int now = n;
        int last = 0;
        cout << "Original number was " << n << endl;
        int count = 0;
        while (last != now) {
            int temp = now;
            last = now;
            vector<int> small;
            if (temp == 0) {
                small.push_back(0);
            }
            while (temp != 0) {
                small.push_back(temp % 10);
                temp /= 10;
            }
            sort(small.begin(), small.end());
            vector<int> big = small;
            reverse(big.begin(), big.end());
            string first_str = "";
            string second_str = "";
            for (int i : big) {
                first_str += to_string(i);
            }
            for (int i : small) {
                second_str += to_string(i);
            }
            int first = stoi(first_str);
            int second = stoi(second_str);
            now = first - second;
            cout << first << " - " << second << " = " << now << endl;
            count++;
        }
        cout << "Chain length " << count << "\n" << endl;
    }
    return 0;
}