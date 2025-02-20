class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        stack = deque()
        trips = sorted(trips,key=lambda x:x[1] )
        total = 0
        for i in trips:
            while stack and stack[0][2] <=i[1]:
                total-= stack[0][0]
                stack.popleft()
            if stack and stack[-1][2] < i[1]:
                stack = deque()
                total = 0
            total += i[0]   
            if total>capacity:
                return False
            stack.append(i)
            x = 2
            while len(stack)>=x and stack[-1*x][2] > i[2]: 
                stack[-1*x],stack[-1*(x-1)] = stack[-1*(x-1)],stack[-1*x]
                x+=1
        return True