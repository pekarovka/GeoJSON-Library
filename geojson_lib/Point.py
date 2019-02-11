from geojson_lib.Geometry import Geometry


class Point(Geometry):
    def __init__(self, json_entity):
        super(Point, self).__init__(json_entity)

        self.lat = self.coordinates[0]
        """Point latitude"""

        self.lon = self.coordinates[1]
        """Point longitude"""

    def getType(self):
        return "Point"
