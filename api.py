import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + "/.."))

from api import app


class TestCVEAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_all_cves(self):
        response = self.app.get('/cves/list')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)  # Response should be a list

    def test_get_cve_by_id(self):
        response = self.app.get('/cves/list?cve_id=CVE-2023-0001')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(response.json, list))  # Should return a list

    def test_get_cve_by_year(self):
        response = self.app.get('/cves/list?year=2023')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)

    def test_get_cve_by_min_score(self):
        response = self.app.get('/cves/list?min_score=7')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)

if __name__ == "__main__":
    unittest.main()
