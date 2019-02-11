import unittest
from geojson_lib.GeoJSON import GeoJSON


class TestMultiPolygon(unittest.TestCase):

    def test_it_saves_to_string(self):
        text = """{"type": "MultiPolygon", "coordinates": [[[[1, 2], [3, 4], [5, 6], [1, 2]]]]}"""
        multipolygon = GeoJSON.loadFromString(text)
        savedtext = multipolygon.saveToString()
        self.assertEqual(text, savedtext)


if __name__ == '__main__':
    unittest.main()