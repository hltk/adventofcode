#include "bits/stdc++.h"
using namespace std;
int main() {
	vector<int> a = {0, 1, 0, -1};
	string u;
	cin >> u;
	vector<int> k;
	for (char c : u) k.push_back(c -'0');
	vector<int> v;
	for (int i = 0; i < 10000; ++i) {
		for (int u : k) v.push_back(u);
	}
	int z = stoi(u.substr(0, 7));
	for (int i = 0; i < 100; ++i) {
		vector<int> L(v.size());
		vector<long long> su(v.size());
		for (int j = 0; j < (int) v.size(); ++j) {
			su[j] = v[j];
			if (j) su[j] += su[j - 1];
		}
		auto getsum = [&](int a, int b) -> long long {
			if (b < 0) return 0;
			if (a > b) return 0;
			a = max(a, 0);
			b = min(b, ((int)v.size()) - 1);
			return (su[b] - (a == 0 ? 0 : su[a - 1]));
		};
		for (int j = 0; j < (int) v.size(); ++j) {
			int it = 0;
			long long r = 0;
			for (int h = -1 ; h < (int) v.size(); h += j + 1) {
				r += (a[it] * getsum(h, h + j));
				it = (it + 1) % 4;
			}
			L[j] = abs((int)(r%10ll));
		}
		v = L;
		printf("%d/100\n", i);
	}
	
	for (int i = 0; i < 8; ++i) {
		cout << v[z + i];
	}
	cout << "\n";
}
