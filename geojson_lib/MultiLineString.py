from geojson_lib.Geometry import Geometry


class MultiLineString(Geometry):
    def __init__(self, *coordinates):
        super(MultiLineString, self).__init__()

        self._coordinates = list(coordinates)

        for line in self._coordinates:
            if len(line) < 2:
                raise Exception("Each line must have at least 2 points.")

    def __len__(self):
        return len(self._coordinates)

    def lat(self, line_index, point_index):
        return self._coordinates[line_index][point_index][0]

    def lon(self, line_index, point_index):
        return self._coordinates[line_index][point_index][1]

    def getType(self):
        return "MultiLineString"

    @classmethod
    def loadFromJsonEntity(cls, json_entity):
        return MultiLineString(*json_entity["coordinates"])

    def saveToJsonEntity(self):
        json_entity = super(MultiLineString, self).saveToJsonEntity()
        json_entity["coordinates"] = self._coordinates
        return json_entity
