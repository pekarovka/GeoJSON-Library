import unittest
from geojson_lib.GeoJSON import GeoJSON


class TestPoint(unittest.TestCase):
    def test_it_loads_geojson_object_from_string(self):
        text = """{"type": "Point", "coordinates": [102.0, 0.5]}"""
        point = GeoJSON.loadFromString(text)
        self.assertEqual(102.0, point.lat)
        self.assertEqual(0.5, point.lon)

    def test_it_returns_point_instance(self):
        text = """{"type": "Point", "coordinates": [102.0, 0.5]}"""
        point = GeoJSON.loadFromString(text)
        self.assertEqual("Point", point.getType())


if __name__ == '__main__':
    unittest.main()
