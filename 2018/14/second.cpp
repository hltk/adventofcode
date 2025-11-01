#include "bits/stdc++.h"
using namespace std;
#define ALL(x) x.begin(), x.end()
#define SZ(x) ((int)(x).size())
#define SORT(x) sort(x.begin(),x.end())
#define REV(x) reverse(x.begin(), x.end())
#define COUNT(x, y) count(x.begin(), x.end(), y)
#define db(...) cout << " [" << #__VA_ARGS__ << ": " << __VA_ARGS__ << "] "
#define F first
#define S second
#define For(i, N) for (int i = 0; i < N; ++i)
#define Gor(i, N) for (int i = 1; i <= N; ++i)
#define pb push_back
#define eb emplace_back
#define mp make_pair
using ii=long long;
using pi=pair<int,int>;
using pii=pair<ii,ii>;
template<typename T>
using vec=vector<T>;

list<int> L;

int main() {
	L.push_back(3);
	L.push_back(7);
	auto it1 = L.begin();
	auto it2 = --L.end();
	
	string in;
	cin >> in;
	auto forward = [&](auto &it) -> void {
		it++;
		if (it == L.end()) it = L.begin();
	};
	deque<int> back6;
	auto add_new = [&](int x) {
		back6.push_back(x);
		if (back6.size() > 6) back6.pop_front();
		L.push_back(x);
		if (back6.size() == 6) {
			int ok = 1;
			for (int j = 0; j < 6; ++j) {
				if (back6[j] != in[j] - '0') ok = 0;
			}
			if (ok) {
				cout << L.size() - back6.size() << "\n";
				exit(0);
			}
		}
	};
	for (;;) {
		int u = *it1 + *it2;
		if (u == 0) add_new(0);
		else if (u < 10) add_new(u);
		else {
			add_new(u / 10);
			add_new(u % 10);
		}
		int a = *it1 + 1;
		while (a--) forward(it1);
		int b = *it2 + 1;
		while (b--) forward(it2);
	}
}
