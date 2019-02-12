from geojson_lib.LinearRingArray import LinearRingArray
from geojson_lib.Geometry import Geometry
from geojson_lib.LinearRing import LinearRing


class Polygon(Geometry):
    def __init__(self, *linear_rings): """RFC GeoJSON format use linear ring and linear rin array."""
        self._linear_ring_array = LinearRingArray(*linear_rings)

    def getType(self):
        return "Polygon"

    @classmethod
    def loadFromJsonEntity(cls, json_entity):
        """Load from entity and return with function map."""
        return Polygon(*map(lambda x: LinearRing(x), json_entity["coordinates"]))

    def saveToJsonEntity(self):
        """Save and return entity."""
        json_entity = super(Polygon, self).saveToJsonEntity()
        json_entity["coordinates"] = self._linear_ring_array.saveToJsonEntity()
        return json_entity
