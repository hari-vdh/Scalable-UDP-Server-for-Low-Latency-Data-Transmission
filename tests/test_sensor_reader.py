import unittest
import time
from src.sensor_reader import SensorReader

class TestSensorReader(unittest.TestCase):
    def setUp(self):
        # Initialize sensor reader and start the update thread
        self.reader = SensorReader()
        self.reader.start()
        # Allow time for the sensor to update at least once
        time.sleep(3)

    def tearDown(self):
        # Ensure the sensor reader thread is properly stopped after tests
        self.reader.stop()

    def test_get_data_structure(self):
        """
        Verify that sensor data returned contains 'humidity', 'temperature', and 'timestamp'.
        """
        data = self.reader.get_data()
        self.assertIsInstance(data, dict)
        self.assertIn("timestamp", data)
        if data.get("status") == "OK":
            self.assertIn("humidity", data)
            self.assertIn("temperature", data)
            self.assertIsInstance(data["humidity"], float)
            self.assertIsInstance(data["temperature"], float)
        else:
            self.assertEqual(data.get("error"), "Sensor reading failed")
    
    def test_self_check(self):
        try:
            self.reader.self_check()
        except Exception as e:
            self.fail(f"self_check raised an exception: {e}")
    
    def test_multiple_data_reads(self):
        readings = []
        for _ in range(5):
            data = self.reader.get_data()
            readings.append(data)
            time.sleep(1)
        valid = any("humidity" in d and "temperature" in d for d in readings if d.get("status") == "OK")
        self.assertTrue(valid or any(d.get("status") == "FAIL" for d in readings))

if __name__ == "__main__":
    unittest.main()
