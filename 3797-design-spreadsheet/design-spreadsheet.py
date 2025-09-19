class Spreadsheet:

    def __init__(self, rows: int):
        self.arr = [[0]*26 for i in range(rows)]
        self.ind = ord("A")

    def setCell(self, cell: str, value: int) -> None:
        self.arr[int(cell[1:])-1][ord(cell[0])-ord("A")] = value
        

    def resetCell(self, cell: str) -> None:
        self.setCell(cell,0)

    def getValue(self, formula: str) -> int:
        c1,c2 = formula[1:].split("+")
        val1 ,val2= 1,1
        if c1[0].isalpha():
            r1 = int(c1[1:])-1 if len(c1)>1 else 0 
            val1 =  self.arr[r1][ord(c1[0])-ord("A")]  if r1<len(self.arr) else 0
        else:
            val1 = int(c1)
        if c2[0].isalpha():
            r2 = int(c2[1:])-1 if len(c2)>1 else 0
            val2 =  self.arr[r2][ord(c2[0])-ord("A")]  if r2<len(self.arr) else 0
        else:
            val2 = int(c2)
        return  val1+val2


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)