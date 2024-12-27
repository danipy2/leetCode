class Solution:
    def removeStars(self, s: str) -> str:
        let = []
        for i in s:
            if i == "*":
                let.pop()
            else:
                let.append(i)
        return "".join(let)
