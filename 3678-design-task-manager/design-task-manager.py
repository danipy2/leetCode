import heapq

class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.task = {}  
        self.heap = []      
        for userId, taskId, priority in tasks:
            self.task[taskId] = (userId, priority)
            heapq.heappush(self.heap, (-priority, -taskId, taskId))

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.task[taskId] = (userId, priority)
        heapq.heappush(self.heap, (-priority, -taskId, taskId))

    def edit(self, taskId: int, newPriority: int) -> None:
        userId, _ = self.task[taskId]
        self.task[taskId] = (userId, newPriority)
        heapq.heappush(self.heap, (-newPriority, -taskId, taskId))

    def rmv(self, taskId: int) -> None:
        if taskId in self.task:
            del self.task[taskId]

    def execTop(self) -> int:
        while self.heap:
            neg_priority, neg_taskId, taskId = heapq.heappop(self.heap)
            if taskId in self.task:
                userId, priority = self.task[taskId]
                
                if -neg_priority == priority:
                    del self.task[taskId]
                    return userId
        return -1