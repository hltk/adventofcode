#include "bits/stdc++.h"
using namespace std;
int main() {
	int r  =0;
	for (int i = 171309; i <= 643603; ++i) {
		string u = to_string(i);
		int ok = 1;
		for (int j = 1; j  < (int) u.size(); ++j) {
			if (u[j] < u[j - 1]) ok = 0;
		}
		int b = 0;
		for (int j = 1; j  < (int) u.size(); ++j) {
			if (u[j] == u[j - 1]) b = 1;
		}
		if (b && ok) r++;
	}
	cout << r << "\n";
}
