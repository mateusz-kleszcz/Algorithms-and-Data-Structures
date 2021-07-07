def left(i): return 2 * i + 1
def right(i): return 2 * i + 2
def parent(i): return (i - 1) // 2


class Structure:
    def __init__(self):
        self.max = []
        self.min = []

    def insertToMax(self, value):
        self.max.append(value)
        n = len(self.max) - 1
        while n > 0 and self.max[n] > self.max[parent(n)]:
            self.max[n], self.max[parent(n)] = self.max[parent(n)], self.max[n]
            n = parent(n)

    def insertToMin(self, value):
        self.min.append(value)
        n = len(self.max) - 1
        while n > 0 and self.min[n] < self.min[parent(n)]:
            self.min[n], self.min[parent(n)] = self.min[parent(n)], self.min[n]
            n = parent(n)

    def deleteFromMax(self):
        root = self.max[0]
        n = len(self.max) - 1
        self.max[0] = self.max[n]
        del self.max[n]
        n -= 1
        i = 0
        while left(i) <= n:
            l = left(i)
            r = right(i)
            if r > n or self.max[l] > self.max[r]:
                self.max[i], self.max[l] = self.max[l], self.max[i]
                i = left(i)
            else:
                self.max[i], self.max[r] = self.max[r], self.max[i]
                i = right(i)
        return root

    def deleteFromMin(self):
        root = self.min[0]
        n = len(self.min) - 1
        self.min[0] = self.min[n]
        del self.min[n]
        n -= 1
        i = 0
        while left(i) <= n:
            l = left(i)
            r = right(i)
            if r > n or self.max[l] < self.max[r]:
                self.min[i], self.min[l] = self.min[l], self.min[i]
                i = left(i)
            else:
                self.min[i], self.min[r] = self.min[r], self.min[i]
                i = right(i)
        return root

    def lenMax(self): return len(self.max)
    def lenMin(self): return len(self.min)

    def rootMax(self): return self.max[0]
    def rootMin(self): return self.min[0]

    def insert(self, value):
        if self.lenMax() == 0:
            self.insertToMax(value)
        elif self.lenMax() == 1 and self.lenMin() == 0:
            if value < self.rootMax():
                self.insertToMax(value)
                m = self.deleteFromMax()
                self.insertToMin(m)
            else:
                self.insertToMin(value)
        else:
            if value > self.rootMax():
                self.insertToMin(value)
            else:
                self.insertToMax(value)
            if self.lenMax() > self.lenMin() + 1:
                m = self.deleteFromMax()
                self.insertToMin(m)
            elif self.lenMax() < self.lenMin():
                m = self.deleteFromMin()
                self.insertToMax(m)

    def getMedian(self):
        if (len(self.max) + len(self.min)) % 2 == 0:
            return (self.max[0] + self.min[0]) / 2
        else:
            return self.min[0]


S = Structure()
S.insert(10)
S.insert(12)
S.insert(8)
S.insert(7)
S.insert(13)
S.insert(14)
print(S.getMedian())