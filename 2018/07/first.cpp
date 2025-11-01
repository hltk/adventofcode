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
	set<int> O;
	vector<int> nodes(lol.rbegin(), lol.rend());
	for (int u : nodes) if (!L[u]) O.insert(u);
	vector<int> o;
	while (O.size()) {
		int x = *O.begin();
		O.erase(x);
		o.push_back(x);
		for (int u : v[x]) if (!--L[u]) O.insert(u);
	}
	for (int u : o) cout << (char)u;
	cout << endl;
}
