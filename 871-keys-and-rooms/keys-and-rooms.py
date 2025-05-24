class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visted = set()
        def dfs(lgth,ind):
            if len(visted) == lgth or ind in visted:
                return
            visted.add(ind)
            for i in rooms[ind]:
                dfs(lgth,i)
        dfs(len(rooms),0)
        if len(visted) == len(rooms):
            return True
        return False