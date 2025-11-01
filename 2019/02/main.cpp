#include <bits/stdc++.h>
using namespace std;
vector<int> V;
int main() {
	int x;
	while (cin >> x) {
		V.push_back(x);
	}
	
	for (int a = 0; a < (int) V.size(); ++a){
		for (int b = 0; b < (int) V.size(); ++b){
			vector<int> v = V;
			v[1]=a;
			v[2]=b;
			for (int i = 0; i < (int) v.size(); ++i) {
				if (v[i] == 99) break;
				if (v[i] == 1) {
					v[v[i + 3] ] = v[v[i + 1] ] + v[v[i + 2] ];
					i += 3;
				}
				else if (v[i] == 2) {
					v[v[i + 3] ] = v[v[i + 1] ] * v[v[i + 2] ];
					i += 3;
				}
				else ++i;
			}
			if (v[0]==19690720) {
				cout << a << " " << b << "\n";
				exit(0);
			}
		}
	}
}
