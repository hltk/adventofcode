#include "bits/stdc++.h"
using namespace std;
char img[6][25];
int main() {
	memset(img, -1, sizeof(img));
	string s;
	cin >> s;
	int N = 25 * 6;
	for (int i = 0; i < (int) s.size(); i += N) {
		string u = s.substr(i, N);
		for (int z = 0; z < N; ++z) {
			char c = u[z];
			int ix = z / 25;
			int jx = z % 25;
			if (img[ix][jx] != -1) continue;
			if (c == '2') continue;
			if (c == '0') img[ix][jx] = '.';
			else img[ix][jx] = '#';
		}
	}
	for (int i = 0; i < 6; ++i) {
		for (int j = 0; j < 25; ++j) cout<<img[i][j]<<" ";
		cout<<"\n";
	}
}
