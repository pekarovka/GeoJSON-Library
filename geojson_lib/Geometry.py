from geojson_lib.GeoJSON import GeoJSON


class Geometry(GeoJSON):
    def __init__(self, json_entity):
        super(Geometry, self).__init__(json_entity)
        self.coordinates = self.json_entity["coordinates"]

