"""
data_formatter.py

Provides functions to format sensor data into various output formats,
such as JSON strings, CSV lines, or custom reports.
"""

import json
import csv
import io

def format_as_json(data):
    """
    Convert dictionary data to a JSON-formatted string.
    """
    return json.dumps(data)

def format_as_csv(data):
    """
    Convert dictionary data to a CSV formatted string.
    """
    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=data.keys())
    writer.writeheader()
    writer.writerow(data)
    return output.getvalue()

def format_as_report(data):
    """
    Create a human-readable report from sensor data.
    """
    report = (f"Sensor Data Report:\n"
              f"---------------------\n"
              f"Temperature: {data.get('temperature', 'N/A')} °C\n"
              f"Humidity   : {data.get('humidity', 'N/A')} %\n"
              f"Timestamp  : {data.get('timestamp', 'N/A')}\n")
    return report
