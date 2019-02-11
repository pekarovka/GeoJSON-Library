import unittest
from geojson_lib.GeoJSON import GeoJSON


class TestPolygon(unittest.TestCase):

    def test_it_saves_to_string(self):
        text = """{"type": "Polygon", "coordinates": [[[1, 2], [3, 4], [5, 6], [1, 2]]]}"""
        polygon = GeoJSON.loadFromString(text)
        savedtext = polygon.saveToString()
        self.assertEqual(text, savedtext)


if __name__ == '__main__':
    unittest.main()
