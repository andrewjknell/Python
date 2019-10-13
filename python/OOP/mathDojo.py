class MathDojo:
    def __init__(self):
    	self.result = 0
    def add(self,*nums):
        for n in nums:
            self.result += n
        return self
    def subtract(self,*nums):
        for y in nums:
            self.result -= y
        return self

md = MathDojo()

md.subtract(3,4,5,6,6,5).add(3,3,3,3,3)
print(md.result)
