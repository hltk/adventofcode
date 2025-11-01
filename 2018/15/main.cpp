#include "bits/stdc++.h"
using namespace std;
#define ALL(x) x.begin(), x.end()
#define SZ(x) ((int)(x).size())
#define SORT(x) sort(x.begin(),x.end())
#define REV(x) reverse(x.begin(), x.end())
#define COUNT(x, y) count(x.begin(), x.end(), y)
#define db(...) //cout << " [" << #__VA_ARGS__ << ": " << __VA_ARGS__ << "] "
#define F first
#define S second
#define For(i, N) for (int i = 0; i < N; ++i)
#define Gor(i, N) for (int i = 1; i <= N; ++i)
#define pb push_back
#define eb emplace_back
#define mp make_pair
using ii=long long;
using pii=pair<int,int>;
template<typename T>
using vec=vector<T>;
const int N = 32;
struct lol {
	// -1 empty, 0 goblin, 1 elf, 2 blocked
	int typ = -1;
	int hp = 200;
	
} asd[N + 3][N + 3], orig[N + 3][N + 3];
int Dist[N + 3][N + 3];
int Vis[N + 3][N + 3];
int run(int elf_pow) {
	memset(Dist, 0, sizeof(Dist));
	memset(Vis, 0, sizeof(Vis));
	memmove(asd, orig, sizeof(orig));
	// TODO
	// Combat only ends when a unit finds no targets during its turn.
	int comp = 0;
	for (int it = 1; ; it += 1) {
		//cout << "round! " << it << "\n";
		//cout << "troops left:\n";
		vector<pair<int, int>> ord;
		for (int i = 1; i <= N; ++i) {
			for (int j = 1; j <= N; ++j) {
				if (asd[i][j].typ < 2 && asd[i][j].typ >= 0)
					ord.emplace_back(i, j);
			}
		}
		for (auto &u : ord) {
			if (asd[u.F][u.S].typ == -1) continue; // dead
			int ctyp = asd[u.F][u.S].typ;
			////cout << "stating to calculate {" << u.F << ", " << u.S << "} type: " << ctyp << "\n";
			
			int ok2 = 0;
			for (int i = 1; i <= N; ++i) {
				for (int j = 1; j <= N; ++j) {
					if (asd[i][j].typ == 1 - ctyp) {
						ok2 = 1;
					}
				}
			}
			if (!ok2) {
				// cout << "completed rounds: " << comp << "\n";
				long long su = 0;
				for (int i = 1; i <= N; ++i) {
					for (int j = 1; j <= N; ++j) {
						int T = asd[i][j].typ;
						if (T != 0 && T != 1) continue;
						su += asd[i][j].hp;
					}
				}
				//cout << "rem hp: " << su << "\n";
				cout << "multiplied: " << su * comp << "\n";
				return 1;
			}
			
			
			// check if already possible to attack
			int ok1 = 0;
			
			for (int i = -1; i <= 1; ++i) {
				for (int j = -1; j <= 1; ++j) {
					if ((i != 0) + (j != 0) != 1) continue;
					if (asd[u.F + i][u.S + j].typ == 1 - ctyp && !ok1) {
						ok1 = 1;
						
					}
				}
			}
			//if (ok1) //cout << "already possible to attack\n";
			if (!ok1) {
				// get the square to attack
				// by doing a bfs
				{
					vector<pair<int, int>> B;
					B.emplace_back(u.F, u.S);
					fill((int*)Dist,(int*)Dist+(N+3)*(N+3),(int)1e9);
					memset(Vis, 0, sizeof(Vis));
					Dist[u.F][u.S] = 0;
					Vis[u.F][u.S] = 1;
					for (int i = 0; i < (int) B.size(); ++i) {
						auto z = B[i];
						for (int it = -1; it <= 1; ++it) {
							for (int jt = -1; jt <= 1; ++jt) {
								if (it == 0 && jt == 0) continue;
								if (it != 0 && jt != 0) continue;
								auto k = z;
								k.F += it;
								k.S += jt;
								if (k.F < 1) continue;
								if (k.S < 1) continue;
								if (k.F > N) continue;
								if (k.S > N) continue;
								if (Vis[k.F][k.S]) continue;
								if (asd[k.F][k.S].typ != -1) continue;
								Dist[k.F][k.S] = Dist[z.F][z.S] + 1;
								Vis[k.F][k.S] = 1;
								B.push_back(k);
							}
						}
					}
				}
				// choose where to go
				int res = 1e9;
				pair<int, int> fi;
				for (int i = 1; i <= N; ++i) {
					for (int j = 1; j <= N; ++j) {
						if (!Vis[i][j]) continue;
						int ok = 0;
						for (int it = -1; it <= 1; ++it) {
							for (int jt = -1; jt <= 1; ++jt) {
								if ((it != 0) + (jt != 0) != 1) continue;
								if (asd[i + it][j + jt].typ == 1 - ctyp) ok = 1;
							}
						}
						if (ok) {
							if (Dist[i][j] < res) {
								fi = {i, j};
								res = Dist[i][j];
							}
						}
					}
				}
				if (res != (int) 1e9) {
					pii dest = fi;
					// calculate distances from the chosen square
					{
						vector<pair<int, int>> B;
						B.emplace_back(dest.F, dest.S);
						fill((int*)Dist,(int*)Dist+(N+1)*(N+1),(int)1e9);
						memset(Vis, 0, sizeof(Vis));
						Dist[dest.F][dest.S] = 0;
						Vis[dest.F][dest.S] = 1;
						for (int i = 0; i < (int) B.size(); ++i) {
							auto z = B[i];
							for (int it = -1; it <= 1; ++it) {
								for (int jt = -1; jt <= 1; ++jt) {
									if (it == 0 && jt == 0) continue;
									if (it != 0 && jt != 0) continue;
									auto k = z;
									k.F += it;
									k.S += jt;
									if (k.F < 1) continue;
									if (k.S < 1) continue;
									if (k.F > N) continue;
									if (k.S > N) continue;
									if (Vis[k.F][k.S]) continue;
									if (asd[k.F][k.S].typ != -1) continue;
									Dist[k.F][k.S] = Dist[z.F][z.S] + 1;
									Vis[k.F][k.S] = 1;
									B.push_back(k);
								}
							}
						}
					}
					Dist[u.F][u.S] = min({Dist[u.F+1][u.S]+1, Dist[u.F-1][u.S]+1, Dist[u.F][u.S+1]+1,Dist[u.F][u.S-1]+1});
					
					// move to the chosen square
					
					if (asd[dest.F][dest.S].typ == ctyp) continue;
					
					pii old = u;
					while (u != dest) {
						int ok = 0;
						for (int it = -1; it <= 1 && !ok; ++it) {
							for (int jt = -1; jt <= 1 && !ok; ++jt) {
								if ((it != 0) + (jt != 0) != 1) continue;
								if (Dist[u.F + it][u.S + jt] == Dist[u.F][u.S] - 1) {
									u.F += it;
									u.S += jt;
									ok = 1;
								}
							}
						}
						assert(ok);
						break;
					}
					swap(asd[old.F][old.S], asd[u.F][u.S]);
				}
			}
			
			ok1 = 0;
			for (int i = -1; i <= 1; ++i) {
				for (int j = -1; j <= 1; ++j) {
					if ((i != 0) + (j != 0) != 1) continue;
					if (asd[u.F + i][u.S + j].typ == 1 - ctyp && !ok1) {
						ok1 = 1;
					}
				}
			}
			
			if (ok1) {
				// //cout << " at range, let's attack \n";
				int res = (int) 1e9;
				pair<int, int> be;
				for (int i = -1; i <= 1; ++i) {
					for (int j = -1; j <= 1; ++j) {
						if ((i != 0) + (j != 0) != 1) continue;
						if (asd[u.F + i][u.S + j].typ == 1 - ctyp) {
							int hp = asd[u.F + i][u.S + j].hp;
							if (hp < res) {
								res = hp;
								be = {u.F + i, u.S + j};
							}
						}
					}
				}
				assert(res != (int) 1e9);
				int z = 0;
				if (ctyp == 1) z = elf_pow;
				else z = 3;
				if ((asd[be.F][be.S].hp -= z) <= 0) {
					if (asd[be.F][be.S].typ == 1) return 0;
					asd[be.F][be.S].typ = -1;
				}
			}
		}
		/*
		//cout << "after: " << it << "\n";
		for (int i = 1; i <= N; ++i) {
			for (int j = 1; j <= N; ++j) {
				int k = asd[i][j].typ;
				if (k == 0) //cout << 'G';
				if (k == 1) //cout << 'E';
				if (k == -1) //cout << ".";
				if (k == 2) //cout << "#";
			}
			//cout << "\n";
		}
		*/
		comp += 1;
	}
	assert(0);
}
int main() {
	for (int i = 1; i <= N; ++i) {
		for (int j = 1; j <= N; ++j) {
			char c;
			cin >> c;
			if (c == 'G') {
				orig[i][j].typ = 0;
			}
			if (c == 'E') {
				orig[i][j].typ = 1;
			}
			if (c == '#') {
				orig[i][j].typ = 2;
			}
		}
	}
	int b = 0;
	for (int z = 1 << 19; z; z /= 2) {
		if (!run(b + z)) b += z;
	}
	cout << b + 1 << "\n";
	assert(run(b + 1));
}
