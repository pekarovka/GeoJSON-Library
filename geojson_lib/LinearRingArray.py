
class LinearRingArray():
    """Represents a set of linear rings (polygon basically)"""

    def __init__(self, *linear_rings):
        self._linear_rings = linear_rings

        if len(self._linear_rings) < 1:
            raise Exception("LinearRingArray has to have at least 1 ring.")

    def saveToJsonEntity(self):
        return list(map(lambda x: x.saveToJsonEntity(), self._linear_rings))

