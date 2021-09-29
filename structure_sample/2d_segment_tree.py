import math
class tree():

    def __init__(self, arr:list):
        N = len(arr)
        self.H = int(math.ceil(math.log2(N)))
        self.tree = [0] * (1<<(self.H+1))
        self.init_tree(arr, 1, 0, N-1)
    
    def __init__(self, N:int):
        self.H = int(math.ceil(math.log2(N)))
        self.tree = [0] * (1<<(self.H+1))
    
    def init_tree(self, arr, idx, start, end):
        if start==end:
            self.tree[idx] = arr[start]
            return arr[start]

        mid = (start+end)//2

        self.tree[idx] = self.init_tree(arr, idx<<1, start, mid) + \
                         self.init_tree(arr,idx<<1|1, mid+1, end)

        return self.tree[idx]    
    
    def update(self, idx, node, start, end, value):
        if start==end:
            self.tree[idx] = value
            return
        
        mid = (start+end)//2

        if(node <= mid):
            self.update(idx<<1, node, start, mid, value)
        else:
            self.update(idx<<1|1, node, mid+1, end, value)
        
        self.tree[idx] = self.tree[idx<<1] + self.tree[idx<<1|1]

    def query(self, idx, left, right, start, end):
        if left<=start and right>=end:
            return self.tree[idx]
        
        ret = 0
        mid = (start+end)//2
        if left<=mid:
            ret  += self.query(idx<<1 , left, right, start, mid)
        if right>mid:
            ret += self.query(idx<<1|1, left, right, mid+1, end)
        
        return ret


class segTree():
    
    def __init__(self, n, m, arr):
        self.n = n
        self.m = m
        self.h = int(math.ceil(math.log2(n)))
        self.col = 1 << (self.h+1)
        self.tree = []
        for i in range(self.col):
            self.tree.append(tree(m))
    
    



    def query(self, idx, x1,y1, x2,y2):
        print()


"""

#include <iostream>
using namespace std;

struct Seg {
	int tree[3030];
	int bias;
	void init(int n) { for (bias = 1; bias < n; bias <<= 1); }
	void update(int x, int v) {
		x += bias; tree[x] = v;
		while (x >>= 1) {
			tree[x] = tree[x << 1] + tree[x << 1 | 1];
		}
	}
	int query(int l, int r) {
		l += bias, r += bias;
		int ret = 0;
		while (l < r) {
			if (l & 1) ret += tree[l++];
			if (!(r & 1)) ret += tree[r--];
			l >>= 1, r >>= 1;
		}
		if (l == r) ret += tree[r];
		return ret;
	}
};

struct Seg2d {
	Seg tree[3030];
	int bias;
	void init(int n, int m) {
		for (bias = 1; bias < n; bias <<= 1);
		for (int i = 0; i <= bias * 2; i++) tree[i].init(m);
	}
	void update(int x, int y, int v) {
		x += bias; tree[x].update(y, v);
		while (x >>= 1) {
			int t1 = tree[x << 1].query(y, y);
			int t2 = tree[x << 1 | 1].query(y, y);
			tree[x].update(y, t1 + t2);
		}
	}
	int query(int l, int r, int ll, int rr) {
		l += bias, r += bias;
		int ret = 0;
		while (l < r) {
			if (l & 1) ret += tree[l++].query(ll, rr);
			if (!(r & 1)) ret += tree[r--].query(ll, rr);
			l >>= 1, r >>= 1;
		}
		if (l == r) ret += tree[r].query(ll, rr);
		return ret;
	}
}seg;

int main() {
	ios_base::sync_with_stdio(0); cin.tie(0);
	int n, m; cin >> n >> m;
	seg.init(n, n);
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= n; j++) {
			int t; cin >> t;
			seg.update(i, j, t);
		}
	}

	while (m--) {
		int op, a, b, c, d; cin >> op;
		if (!op) {
			cin >> a >> b >> c;
			seg.update(a, b, c);
		}
		else {
			cin >> a >> c >> b >> d;
			cout << seg.query(a, b, c, d) << "\n";
		}
	}
}

"""
