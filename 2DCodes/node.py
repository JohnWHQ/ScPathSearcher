
class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def __repr__(self):
        return "({}, {})".format(self.x, self.y)

    def __hash__(self):
        return hash("{}_{}".format(self.x,self.y))

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
