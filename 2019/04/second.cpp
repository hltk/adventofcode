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
		for (int j = 0; j  < (int) u.size(); ++j) {
			int h = j;
			while (h + 1 < (int) u.size() && u[h +1] == u[j]) ++h;
			if (h - j + 1 == 2) b = 1;
			j = h;
		}
		if (b && ok) r++;
		
	}
	cout << r << "\n";
}
