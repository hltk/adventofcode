#include "bits/stdc++.h"
using namespace std;
vector<int> v[256];
int L[256];
int main() {
	set<char> lol;
	char a, b;
	while (cin >> a >> b) {
		// a ennen b:tä
		lol.insert(a);
		lol.insert(b);
		v[a].push_back(b);
		L[b]++;
	}
	vector<int> nodes(lol.rbegin(), lol.rend());
	vector<int> time(256);
	vector<int> proc(256);
	int c = nodes.size();
	multiset<int> ASD;
	for (int j = 0; j< 5; ++j) ASD.insert(0);
	int j = 0;
	for (; c; ++j) {
		for (int i : nodes) {
			if (!L[i] && time[i] <= j && !proc[i]) {
				if (*ASD.begin() > j) time[i]++;
				else {
					proc[i] = 1;
					--c;
					ASD.erase(ASD.begin());
					int end = j + i - 'A' + 1 + 60;
					ASD.insert(end);
					for (int u : v[i]) {
						L[u]--;
						time[u] = max(time[u], end);
					}
				}
			}
		}
	}
	cout << *ASD.rbegin() << "\n";
}
