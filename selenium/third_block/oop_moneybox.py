class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0

    def can_add(self, v):
        if self.count + v <= self.capacity:
            rez = True
        else:
            rez = False
        return rez

    def add(self, v):
        if self.can_add(v) == True:
            self.count += v
