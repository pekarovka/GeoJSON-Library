from geojson_lib.Geometry import Geometry


class MultiPoint(Geometry):
    def __init__(self, json_entity):
        super(MultiPoint, self).__init__(json_entity)

        self._coordinates = json_entity["coordinates"]

    def __len__(self):
        return len(self._coordinates)

    def lat(self, index):
        return self._coordinates[index][0]

    def lon(self, index):
        return self._coordinates[index][1]

    def getType(self):
        return "MultiPoint"

    def saveToJsonEntity(self):
        json_entity = super(MultiPoint, self).saveToJsonEntity()
        json_entity["coordinates"] = self._coordinates
        return json_entity
