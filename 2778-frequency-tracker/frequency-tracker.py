class FrequencyTracker:

    def __init__(self):
        self.new = {}
        self.freq = {}


    def add(self, number: int) -> None:
        f =  self.new.get(number,0)
        if f in self.freq :
            self.freq[f]-=1
            if self.freq[f] == 0:
                del self.freq[f]
        self.freq[f+1] = self.freq.get(f+1,0)+1
        self.new[number] = self.new.get(number,0)+1


    def deleteOne(self, number: int) -> None:
        if number in self.new:
            f = self.new.get(number,0)
            if f in self.freq:
                self.freq[f]-=1
                if self.freq[f] == 0:
                    del self.freq[f]
            self.new[number] = self.new.get(number,1)-1
            if self.new[number]==0:
                del self.new[number]
            self.freq[f-1] = self.freq.get(f-1,0)+1
        

    def hasFrequency(self, frequency: int) -> bool:
        return frequency in self.freq
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)