
class LinearRing():
    def __init__(self, points):
        self._points = points

        if len(points) < 4:
            raise Exception("LinearRing must have at least 4 points.")

        if points[0] != points[-1]:
            raise Exception("First point does not equal the last point.")

    def saveToJsonEntity(self):
        return self._points
