import unittest
from geojson_lib.GeoJSON import GeoJSON


class TestGeoJson(unittest.TestCase):
    def test_it_loads_geojson_object_from_string(self):
        text = """{"type": "Point", "coordinates": [102.0, 0.5]}"""
        point = GeoJSON.loadFromString(text)
        self.assertEqual("Point", point.json_entity["type"])
        self.assertEqual(102.0, point.json_entity["coordinates"][0])


if __name__ == '__main__':
    unittest.main()
