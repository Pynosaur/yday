#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: @spacemany2k38
# 2025-12-24

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app.core.date_calc import get_day_of_year


class TestYday(unittest.TestCase):
    """Test cases for yday command."""
    
    def test_day_range(self):
        """Test that day of year is in valid range (1-366)."""
        day = get_day_of_year()
        self.assertGreaterEqual(day, 1, "Day should be >= 1")
        self.assertLessEqual(day, 366, "Day should be <= 366")


if __name__ == "__main__":
    unittest.main()

