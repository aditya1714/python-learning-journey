class zen:
    def __init__(self, n):
        self.n = n

    def __add__(self, num):
        return self.n + num.n
    
n = zen(1)
m = zen(2)

print(n + m)