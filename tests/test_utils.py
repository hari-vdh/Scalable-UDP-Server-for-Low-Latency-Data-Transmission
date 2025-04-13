import unittest
from src.utils.data_formatter import format_as_json, format_as_csv, format_as_report

class TestDataFormatter(unittest.TestCase):
    def setUp(self):
        self.sample_data = {
            "humidity": 55.5,
            "temperature": 22.3,
            "timestamp": "2025-01-01 12:34:56"
        }

    def test_format_as_json(self):
        json_output = format_as_json(self.sample_data)
        self.assertTrue(isinstance(json_output, str))
        self.assertIn("humidity", json_output)

    def test_format_as_csv(self):
        csv_output = format_as_csv(self.sample_data)
        self.assertTrue(isinstance(csv_output, str))
        self.assertIn("temperature", csv_output)

    def test_format_as_report(self):
        report = format_as_report(self.sample_data)
        self.assertIn("Temperature", report)
        self.assertIn("Humidity", report)

if __name__ == "__main__":
    unittest.main()
