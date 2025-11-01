#include <bits/stdc++.h>
using namespace std;
int main() {
	long long x;
	long long r = 0;
	while (cin >> x) {
		x /= 3;
		x -= 2;
		while (x > 0) {
			r += x;
			x /= 3;
			x -= 2;
		}
	}
	cout << r << "\n";
}
