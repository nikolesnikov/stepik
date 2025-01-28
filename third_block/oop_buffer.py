class Buffer:
    def __init__(self):
        self.ls = []

    def add(self, *a):
        self.ls += list(a)
        while len(self.ls) >= 5:
            print(sum(self.ls[0:4]))
            del self.ls[0:4]

    def get_current_part(self):
        return self.ls
