#pragma GCC optimize "-O3"
#pragma GCC optimize "unroll-loops"
#include "bits/stdc++.h"
using namespace std;
const int M = 4000;
int Dist(int a, int b, int c, int d) {
	return abs(a - c) + abs(b - d);
}

int main() {
	const int N = 50;
	vector<pair<int, int>> v(N);
	for (int i = 0; i < N; ++i) {
		cin >> v[i].first >> v[i].second;
	}
	long long r = 0;
	for (int i = -M; i <= M; ++i) {
		for (int j = -M; j <= M; ++j) {
			long long su = 0;
			for (int h = 0; h < N; ++h) {
				su += Dist(i, j, v[h].first, v[h].second);
			}
			if (su < 10000) ++r;
		}
	}
	cout << r << "\n";
}
