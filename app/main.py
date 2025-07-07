# -*- coding: utf-8 -*-
#
# yday - Get current day of year
#
# Author: vvrmatos (@spacemany2k38)
# Date: 2025-07-07
# Description: Simple utility to get the current day of the year
# License: CC0 1.0 Universal
#
# This module provides a function to calculate and return the current
# day of the year (1-366, accounting for leap years).
#

#!/usr/bin/env python3

import datetime


def get_year_day() -> int:
	yday = datetime.date.today().timetuple().tm_yday
	return yday

def main():
	print(get_year_day())
	
if __name__ == '__main__':
	main()
