class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        r = 0
        output = []
        for i in range(len(firstList)):
            while r<len(secondList):
                if firstList[i][0] >= secondList[r][0] and firstList[i][1] <= secondList[r][1]:
                    output.append([firstList[i][0],firstList[i][1]])
                elif firstList[i][0] <= secondList[r][0] and firstList[i][1] >= secondList[r][1]:
                    output.append([secondList[r][0],secondList[r][1]])
                elif  firstList[i][1] >= secondList[r][1] and firstList[i][0] <= secondList[r][1]:
                    output.append([firstList[i][0],secondList[r][1]])
                elif  firstList[i][1] >= secondList[r][0] and firstList[i][0] <= secondList[r][0]:
                    output.append([secondList[r][0],firstList[i][1]])
                
                
                r+=1
            r = 0
        return output
            