#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: @spacemany2k38
# 2025-12-24

import datetime


def get_day_of_year():
    """Return the current day of the year (1-366)."""
    today = datetime.date.today()
    return today.timetuple().tm_yday
