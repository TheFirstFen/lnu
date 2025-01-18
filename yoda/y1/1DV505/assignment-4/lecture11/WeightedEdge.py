from misc.Graph import Edge


class WeightedEdge(Edge):
    def __init__(self, u, v, weight):
        super().__init__(u, v)
        self.weight = weight

    def __lt__(self, other):
        return self.weight > other.weight

    def __le__(self, other):
        return self.weight >= other.weight

    def __gt__(self, other):
        self.weight < other.weight

    def __ge__(self, other):
        self.weight <= other.weight

    def __eq__(self, other):
        self.weight == other.weight

    def __ne__(self, other):
        self.weight != other.weight