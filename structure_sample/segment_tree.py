 
class Tree():
    table = [0]* 10000000
    def __init__(self):
        print("tree")
    
    def init(self, cur, arr, left ,right):
        if left==right:
            self.table[cur] = arr[left]
        mid = (left+right)//2

        self.table[cur] = self.init(cur*2,arr, left, mid) + self.init(cur*2+1, arr, mid+1, right)

    def search(self, cur, left, right, start, end):# left-right 검색하고자 하는 구간
        if left <= start and right >= end:
            return self.table[cur]
        
        ret = 0
        mid = (start+end)//2
        if left<=mid:
            ret  += self.search(cur*2, left, right, start, mid)
        if right>mid:
            ret += self.search(cur*2+1, left,right, mid+1, end)
        
        return ret
    
    def update(self, cur, idx, value, left, right):
        if left==right:
            self.table[cur] = value
        
        mid = (left+right)//2
        if idx <= mid:
            self.update(cur*2, idx, value, left, mid)
        else:
            self.update(cur*2+1, idx, value, mid+1, right)
        
        self.table[cur] = self.table[cur*2] +self.table[cur*2+1]
    
