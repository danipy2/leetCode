class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        list_ = []
        for i in range(1,n+1):
            list_.append(i)
        start = 0
        while(len(list_)>1):
            tobe_removed = ((start+k-1)%len(list_))
            list_.pop(tobe_removed)
            start = tobe_removed
        return list_[0]


        