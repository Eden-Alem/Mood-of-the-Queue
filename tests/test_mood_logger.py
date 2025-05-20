import pytest
from src.mood_logger import log_mood

class MockSheet:
    def __init__(self):
        self.data = []
    def append_row(self, row):
        self.data.append(row)
    def get_all_records(self):
        return [{"timestamp": row[0], "mood": row[1], "note": row[2]} for row in self.data]

def test_log_mood():
    sheet = MockSheet()
    log_mood(sheet, "😊", "Test happy note")
    assert len(sheet.data) == 1
    assert sheet.data[0][1] == "😊"
