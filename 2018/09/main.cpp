#include "bits/stdc++.h"
using namespace std;

list<int> circ;
list<int>::iterator it;

void forward() {
	++it;
	if (it == circ.end()) it = circ.begin();
}
void backward() {
	if (it == circ.begin()) it = --circ.end();
	else --it;
}
int main() {
	int N, M;
	scanf("%d%d", &N, &M);
	circ.push_back(0);
	it = circ.begin();
	vector<long long> scores(N);
	for (int i = 1; i <= M; ++i) {
		if (i % 23 == 0) {
			scores[(i - 1) % N] += i;
			for (int j = 0; j < 7; ++j) backward();
			scores[(i - 1) % N] += *it;
			it = circ.erase(it);
		} else {
			forward();
			forward();
			it = circ.insert(it, i);
		}
	}
	cout << *max_element(scores.begin(), scores.end()) << "\n";
}
