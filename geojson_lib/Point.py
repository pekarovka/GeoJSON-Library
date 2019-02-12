from geojson_lib.Geometry import Geometry


class Point(Geometry):
    def __init__(self, lat, lon):
        super(Point, self).__init__()

        self.lat = lat
        """Point latitude"""

        self.lon = lon
        """Point longitude"""

    def getType(self):
        return "Point"

    @classmethod
    def loadFromJsonEntity(cls, json_entity):
        """Load from entity."""
        return Point(json_entity["coordinates"][0], json_entity["coordinates"][1])

    def saveToJsonEntity(self):
        """Save and return entiny."""
        json_entity = super(Point, self).saveToJsonEntity()
        json_entity["coordinates"] = [self.lat, self.lon]
        return json_entity

