import unittest
from geojson_lib.GeoJSON import GeoJSON


class TestMultiPoint(unittest.TestCase):
    def test_it_loads_geojson_object_from_string(self):
        text = """{"type": "MultiPoint", "coordinates": [[101, 0.6], [102.0, 0.5]]}"""
        multipoint = GeoJSON.loadFromString(text)
        self.assertEqual(102.0, multipoint.lat(1))
        self.assertEqual(0.6, multipoint.lon(0))
        self.assertEqual(2, len(multipoint))

    def test_it_returns_point_instance(self):
        text = """{"type": "MultiPoint", "coordinates": [[101, 0.6], [102.0, 0.5]]}"""
        multipoint = GeoJSON.loadFromString(text)
        self.assertEqual("MultiPoint", multipoint.getType())

    def test_it_saves_to_string(self):
        text = """{"type": "MultiPoint", "coordinates": [[101, 0.6], [102.0, 0.5]]}"""
        multipoint = GeoJSON.loadFromString(text)
        savedtext = multipoint.saveToString()
        self.assertEqual(text, savedtext)


if __name__ == '__main__':
    unittest.main()
