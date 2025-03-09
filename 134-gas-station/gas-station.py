class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        compute = []
        total = 0
        start = 0
        for i in range(len(cost)*2):
            total += gas[i%len(cost)]-cost[i%len(cost)]
            if total <0:
                start = i+1
                total = 0
            if start >= len(cost):
                return -1
                break
            if start!= i and i%len(cost) ==start:
                return start
        return start
        