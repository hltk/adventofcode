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
int main() {
	vector<vector<long long>> V(4, vector<long long>(3)), G(4, vector<long long>(3));
	const int N = 4;
	For(i, 4) {
		int a, b, c;
		cin >> a >> b >> c;
		V[i] = {a, b, c};
	}
	for (int it = 0; it < 1000; ++it) {
		for (int i = 0; i < N; ++i) {
			for (int j = i + 1; j < N; ++j) {
				for (int h = 0; h  < 3; ++h) {
					if (V[i][h] == V[j][h]) continue;
					if (V[i][h] < V[j][h]) G[i][h]++, G[j][h]--;
					else G[i][h]--, G[j][h]++;
				}
			}
		}
		for (int i = 0; i < N; ++i) {
			for (int h = 0; h < 3; ++h) {
				V[i][h] += G[i][h];
				//cout << V[i][h] << " ";
			}
			//cout << "\n";
		}
	}
	long long S = 0;
	for (int i = 0; i < N; ++i) {
		long long asd = 0;
		for (int h = 0; h < 3; ++h) asd += abs(V[i][h]);
		long long dsa = 0;
		for (int h = 0; h < 3; ++h) dsa += abs(G[i][h]);
		S += asd * dsa;
	}
	cout << S << "\n";
}
