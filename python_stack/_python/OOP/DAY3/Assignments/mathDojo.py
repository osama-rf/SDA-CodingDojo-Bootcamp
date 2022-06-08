class MathDojo:
    def __init__(self) -> None:
        self.result = 0

    def add(self, *num):
        for i in range(0, len(num)):
            if type(num[i]) is list or type(num[i]) is tuple:
                for val in num[i]:
                    self.result += val
                else:
                    self.result += self.result
            return self
    
    def subtract(self, *num):
        for i in range(0, len(num)):
            if type(num[i]) is list or type(num[i]) is tuple:
                for val in num[i]:
                    self.result -= val
                else:
                    self.result -= self.result
            return self

    def results(self):
        print(self.result)
                



md = MathDojo()

x = md.add(2).add(200,5,1).subtract(3,2).add([3, 5, 7, 8], [2, 4.3, 125]).results()
print(x)

y = md.subtract([1],3,4).add([3, 5, 7, 8], [2, 4.3, 1.25]).subtract(2, [2,3], [1.1, 2.3]).results()
print(y)


