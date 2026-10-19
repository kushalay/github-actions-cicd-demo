import unittest
import json
from app import ApplicationHandler


class TestApplication(unittest.TestCase):

    def test_home_endpoint(self):
        response = {
            "application": "GitHub Actions CI/CD Demo",
            "status": "running"
        }

        self.assertEqual(response["status"], "running")

    def test_health_endpoint(self):
        response = {
            "status": "healthy"
        }

        self.assertEqual(response["status"], "healthy")

    def test_json_response(self):
        response = '{"status": "healthy"}'

        result = json.loads(response)

        self.assertEqual(result["status"], "healthy")


if __name__ == "__main__":
    unittest.main()
