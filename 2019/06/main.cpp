#include "bits/stdc++.h"
using namespace std;
map<string, vector<string>> M;
long long R = 0;
map<string, int> vis;
map<string, int> cnt;
void haku(string s) {
	if (vis[s]) return;
	vis[s] = 1;
	for (auto u : M[s]) {
		haku(u);
		cnt[s] += cnt[u] + 1;
	}
	R += cnt[s];
}
void etsi(string s) {
	if (vis[s]) return;
	if (s == "SAN") {
		cnt[s] = 0;
		return;
	} else cnt[s] = (int) 1e9;
	vis[s] = 1;
	for (auto u : M[s]) {
		etsi(u);
		cnt[s] = min(cnt[s], cnt[u] + 1);
	}
	
}
int main() {
	string k;
	while (cin >> k) {
		string a = k.substr(0, 3);
		string b = k.substr(4);
		M[a];
		M[a].push_back(b);
		M[b].push_back(a);
	}
	etsi("YOU");
	cout << cnt["YOU"]- 1;
	/*
	for (auto [x, y] : M) haku(x);
	cout << R << "\n";
	*/
}
