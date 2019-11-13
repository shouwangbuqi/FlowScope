# min tree, which can fetch min value in log time
import math
class MinTree:
    def __init__(self, degrees):
        self.height = int(math.ceil(math.log(len(degrees), 2)))
        self.numLeaves = 2 ** self.height  
        self.numBranches = self.numLeaves - 1
        self.n = self.numBranches + self.numLeaves
        self.nodes = [float('inf')] * self.n
        for i in range(len(degrees)):
            self.nodes[self.numBranches + i] = degrees[i]
        for i in reversed(range(self.numBranches)):
            self.nodes[i] = min(self.nodes[2 * i + 1], self.nodes[2 * i + 2])

    
    def getMin(self):
        cur = 0
        for i in range(self.height):
            cur = (2 * cur + 1) if self.nodes[2 * cur + 1] <= self.nodes[2 * cur + 2] else (2 * cur + 2)  
        
        return (cur - self.numBranches, self.nodes[cur])

    def index_of(self ,idx):
        cur = self.numBranches + idx
        return self.nodes[cur]

    def setter(self, idx, new_value):
        cur = self.numBranches + idx
        self.nodes[cur] = new_value
        for i in range(self.height):
            cur = (cur - 1) // 2
            nextParent = min(self.nodes[2 * cur + 1], self.nodes[2 * cur + 2])
            if self.nodes[cur] == nextParent:
                break
            self.nodes[cur] = nextParent
        return new_value

    
    def changeVal(self, idx, delta):
        cur = self.numBranches + idx
        if self.nodes[cur] == float('inf'):
            
            return float('inf')

        new_value = self.nodes[cur] + delta
        self.nodes[cur] = new_value

        for i in range(self.height):
            cur = (cur - 1) // 2
            nextParent = min(self.nodes[2 * cur + 1], self.nodes[2 * cur + 2])
            if self.nodes[cur] == nextParent:
                break
            self.nodes[cur] = nextParent
        return new_value


    def dump(self):
        print "numLeaves: %d, numBranches: %d, n: %d, nodes: " % (self.numLeaves, self.numBranches, self.n)
        cur = 0
        for i in range(self.height + 1):
            for j in range(2 ** i):
                print self.nodes[cur],
                cur += 1
            print ''
