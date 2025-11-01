#include "bits/stdc++.h"
using namespace std;

int D[1001000];
long long val[1001000];

// returns end coordinate
int parse(int x) {
	int a, b;
	a = D[x];
	b = D[x + 1];
	int end = x + 2;
	vector<int> laps;
	for (int j = 0; j < a; ++j) {
		laps.push_back(end);
		end = parse(end) + 1;
	}
	if (laps.empty()) {
		long long r = 0;
		for (int j = end; j < end + b; ++j) r += D[j];
		val[x] = r;
	} else {
		long long r = 0;
		for (int j = end; j < end + b; ++j) {
			if (!D[j]) continue;
			if (D[j] - 1 >= laps.size()) continue;
			r += val[laps[D[j] - 1]];
		}
		val[x] = r;
	}
	return end + b - 1;
}

int main() {
	int it = 0, x;
	while (cin >> x) {
		D[++it] = x;
	}
	assert(parse(1) == it);
	cout << val[1] << "\n";
}
