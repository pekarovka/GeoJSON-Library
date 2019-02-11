import unittest
from geojson_lib.GeoJSON import GeoJSON


class TestGeometryCollection(unittest.TestCase):

    def test_it_saves_to_string(self):
        text = """{"type": "GeometryCollection", "geometries": [{"type": "Point", "coordinates": [102.0, 0.5]}]}"""
        geometrycollection = GeoJSON.loadFromString(text)
        savedtext = geometrycollection.saveToString()
        self.assertEqual(text, savedtext)


if __name__ == '__main__':
    unittest.main()