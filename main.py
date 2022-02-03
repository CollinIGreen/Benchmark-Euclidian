import timeit
from memory_profiler import profile

class whileEuclidean:
    def __init__(self):
        self.M = 16
        self.N = 22
    def stupid_Backpedal(self):
        self.runWhileEuclid(self.M, self.N)
    #@profile
    def runWhileEuclid(self, a, b):
        M = a
        N = b
        while M > 0:
            L = N % M
            N = M
            M = L
        return N

class recursiveEuclidean:
    def __init__(self):
        self.M = 16
        self.N = 22
    def defineRecursive(self):
        self.N = int(input("choose a number"))
        self.M = int(input("choose a number smaller than your last number"))
    def stupid_Backpedal(self):
        self.runRecursiveEuclid(self.M, self.N)
    #@profile
    def runRecursiveEuclid(self, a, b):
        M = a
        N = b
        if M > 0:
            L = N % M
            N = M
            M = L
            self.runRecursiveEuclid(M, N)
        return N
Recursion = recursiveEuclidean()
While = whileEuclidean()
While.stupid_Backpedal()
Recursion.stupid_Backpedal
print(timeit.timeit(While.stupid_Backpedal, number=1000))
print(timeit.timeit(Recursion.stupid_Backpedal, number=1000))
