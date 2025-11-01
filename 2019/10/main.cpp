#include "bits/stdc++.h"
using namespace std;
const int N =33;
int d[N+2][N+2];
int main() {
	vector<pair<int, int>> pos;
	for (int i = 1; i <= N; ++i) {
		for (int j = 1; j <= N; ++j) {
			char c;
			cin >> c;
			d[i][j] = c == '#';
			if (d[i][j]) pos.emplace_back(i, j);
		}
	}
	int r = 0;
	for (int i = 1; i <= N; ++i) {
		for (int j = 1; j <= N; ++j) {
			if (!d[i][j]) continue;
			map<pair<int, int>, int> asd;
			for (auto [x, y] : pos) {
				int ai = i - x;
				int aj = j - y;
				if (ai == 0 && aj == 0) continue;
				int u = abs(__gcd(ai, aj));
				ai /= u;
				aj /= u;
				asd[make_pair(ai, aj)]++;
			}
			r = max(r, (int) asd.size());
		}
	}
	for (int i = 1; i <= N; ++i) {
		for (int j = 1; j <= N; ++j) {
			if (!d[i][j]) continue;
			map<pair<int, int>, int> asd;
			for (auto [x, y] : pos) {
				int ai = i - x;
				int aj = j - y;
				if (ai == 0 && aj == 0) continue;
				int u = abs(__gcd(ai, aj));
				ai /= u;
				aj /= u;
				asd[make_pair(ai, aj)]++;
			}
			if ((int)asd.size() == r) {
				using pii = pair<int, int>;
				vector<pair<pii, pii>> v;
				for (auto [x, y] : pos) {
					int ai = i - x;
					int aj = j - y;
					if (ai == 0 && aj == 0) continue;
					v.emplace_back(make_pair(ai, aj), make_pair(x, y));
				}
				sort(v.begin(), v.end(), [](auto ax, auto bx) -> bool {
					auto a = ax.first;
					auto b = bx.first;
					a.second = -a.second;
					b.second = -b.second;
					if (a.second >= 0 && b.second < 0) return 1;
					if (a.second < 0 && b.second >= 0) return 0;
					if (a.second == 0 && b.second == 0) {
						if ((a.first < 0) != (b.first < 0)) {
							return a.first > 0;
						}
						return abs(a.first) < abs(b.first);
					}
    					int D = a.second * b.first - b.second * a.first;
					if (D < 0) return 1;
					if (D > 0) return 0;
					return a.second * a.second + a.first * a.first < b.second * b.second + b.first * b.first;
				});
				pair<int, int> prev = {0, 0};
				int c = 200;
				vector<int> used(v.size());
				auto lmao = [](pair<int, int> x) {
					int u = abs(__gcd(x.first, x.second));
					x.first /= u;
					x.second /= u;
					return x;
				};
				for (int i = 0; ; i = (i + 1) % (int) v.size()) {
					if (lmao(v[i].first) == prev) continue;
					if (used[i]) continue;
					used[i] = 1;
					prev = lmao(v[i].first);
					c--;
					if (c == 0) {
						cout << 100 * (v[i].second.second - 1) + (v[i].second.first - 1) << "\n";
						exit(0);
					}
				}
			}
		}
	}
}
