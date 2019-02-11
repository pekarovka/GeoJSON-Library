from geojson_lib.Geometry import Geometry


class LineString(Geometry):
    def __init__(self, *coordinates):
        super(LineString, self).__init__()

        self._coordinates = list(coordinates)

        if len(self) < 2:
            raise Exception("LineString must have at least 2 points.")

    def __len__(self):
        return len(self._coordinates)

    def lat(self, index):
        return self._coordinates[index][0]

    def lon(self, index):
        return self._coordinates[index][1]

    def getType(self):
        return "LineString"

    @classmethod
    def loadFromJsonEntity(cls, json_entity):
        return LineString(*json_entity["coordinates"])

    def saveToJsonEntity(self):
        json_entity = super(LineString, self).saveToJsonEntity()
        json_entity["coordinates"] = self._coordinates
        return json_entity
