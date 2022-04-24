
class Node:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return "({}, {}, {})".format(self.x, self.y, self.z)

    def __repr__(self):
        return "({}, {}, {})".format(self.x, self.y, self.z)

    def __hash__(self):
        return hash("{}_{}".format(self.x, self.y, self.z))

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
