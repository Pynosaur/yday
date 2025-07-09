#!/usr/bin/env python3

import sys
import datetime
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "app"))

from core.calculator import get_year_day

class TestYearDay(unittest.TestCase):
    
    def test_today_matches(self):
        expected = datetime.date.today().timetuple().tm_yday
        self.assertEqual(get_year_day(), expected)

if __name__ == '__main__':
    unittest.main()
