#pragma GCC optimize "-O3"
#pragma GCC optimize "unroll-loops"
#include "bits/stdc++.h"
using namespace std;

const int M = 10100;
int Grid[M][M];

int Dist(int a, int b, int c, int d) {
	return abs(a - c) + abs(b - d);
}

int main() {
	const int N = 50;
	vector<pair<int, int>> v(N);
	for (int i = 0; i < N; ++i) {
		cin >> v[i].first >> v[i].second;
		v[i].first += M / 2;
		v[i].second += M / 2;
	}
	cout << "input\n";
	for (int i = 0; i < M; ++i) {
		for (int j = 0; j < M; ++j) {
			int best = (int) 1e9;
			int best_it = 0;
			for (int h = 0; h < N; ++h) {
				int A = Dist(i, j, v[h].first, v[h].second);
				if (A == best) best_it = -1;
				if (A < best) {
					best = A;
					best_it = h;
				}
			}
			Grid[i][j] = best_it;
		}
		cout << "done: " << i << "\n";
	}
	cout << "calc\n";
	unordered_set<int> inf;
	for (int i = 0; i < M; ++i) {
		inf.insert(Grid[i][0]);
		inf.insert(Grid[i][M - 1]);
		inf.insert(Grid[0][i]);
		inf.insert(Grid[M - 1][i]);
	}
	inf.insert(-1);
	vector<int> res(N);
	for (int i = 0; i < M; ++i) {
		for (int j = 0; j < M; ++j) {
			if (inf.count(Grid[i][j])) continue;
			res[Grid[i][j]]++;
		}
	}
	cout << *max_element(res.begin(), res.end()) << "\n";
}
