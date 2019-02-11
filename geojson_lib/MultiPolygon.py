from geojson_lib.Geometry import Geometry
from geojson_lib.LinearRing import LinearRing
from geojson_lib.LinearRingArray import LinearRingArray


class MultiPolygon(Geometry):
    def __init__(self, *linear_ring_arrays):
        for a in linear_ring_arrays:
            assert type(a) == LinearRingArray

        self._linear_ring_arrays = linear_ring_arrays

    def getType(self):
        return "MultiPolygon"

    @classmethod
    def loadFromJsonEntity(cls, json_entity):
        return MultiPolygon(*map(
            lambda x: LinearRingArray(*list(map(lambda y: LinearRing(y), x))), json_entity["coordinates"]
        ))

    def saveToJsonEntity(self):
        json_entity = super(MultiPolygon, self).saveToJsonEntity()
        json_entity["coordinates"] = list(map(lambda x: x.saveToJsonEntity(), self._linear_ring_arrays))
        return json_entity
