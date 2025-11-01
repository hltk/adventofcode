#include "bits/stdc++.h"
using namespace std;

const int N = 301;
int val[N][N];

long long su[N][N];

int main() {
	int serial = 0;
	cin >> serial;
	for (int i = 1; i < N; ++i) {
		for (int j = 1; j < N; ++j) {
			long long id = j + 10;
			long long lvl = id * i;
			lvl += serial;
			lvl *= id;
			lvl /= 100;
			lvl %= 10;
			lvl -= 5;
			val[i][j] = lvl;
			su[i][j] = su[i - 1][j] + su[i][j - 1] - su[i - 1][j - 1] + lvl;
		}
	}
	auto getsum = [&](int a, int b, int c, int d) {
		return su[c][d] - su[a - 1][d] - su[c][b - 1] + su[a - 1][b - 1];
	};
	pair<long long, vector<int>> mx{0, {0}};
	for (int i = 1; i < N; ++i) {
		for (int j = 1; j < N; ++j) {
			for (int k = 1; k < N; ++k) {
				if (i + k > N || j + k > N) break;
				mx = max(mx, make_pair(getsum(i, j, i + k - 1, j + k - 1), (vector<int>){j,i,k}));
			}
		}
	}
	for (int u : mx.second) cout << u <<",";
	cout<<"\n";
}
