#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: @spacemany2k38
# 2025-12-24

import datetime
import calendar
import locale


def get_day_of_year():
    """Return the current day of the year (1-366)."""
    today = datetime.date.today()
    return today.timetuple().tm_yday


def get_week_of_year():
    """Return the current week number of the year (ISO week)."""
    today = datetime.date.today()
    return today.isocalendar()[1]


def get_day_name():
    """Return the full name of the current day in lowercase (localized according to system)."""
    today = datetime.date.today()
    # Try to use system locale for localized day names
    try:
        # Save current locale
        old_locale = locale.getlocale(locale.LC_TIME)
        # Set to system default
        locale.setlocale(locale.LC_TIME, '')
        day_name = today.strftime('%A').lower()  # %A for full name, lowercase
        # Restore locale
        locale.setlocale(locale.LC_TIME, old_locale)
        return day_name
    except:
        # Fallback to English if locale fails
        return today.strftime('%A').lower()


def get_month_calendar():
    """Return a formatted calendar for the current month with current day highlighted."""
    today = datetime.date.today()
    year = today.year
    month = today.month
    current_day = today.day
    
    # Get the calendar text
    cal = calendar.TextCalendar(calendar.SUNDAY)
    cal_text = cal.formatmonth(year, month)
    
    # Highlight the current day using ANSI escape codes
    # ANSI codes: \033[7m for reverse video (highlight), \033[0m to reset
    lines = cal_text.split('\n')
    result_lines = []
    
    for line in lines:
        # Skip header lines (month/year and day names)
        if any(day in line for day in ['Su', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa']) or str(year) in line.replace(' ', ''):
            result_lines.append(line)
            continue
        
        # For date lines, highlight the current day
        # Need to be careful with spacing - days are right-aligned in 2-char or 3-char fields
        modified_line = line
        
        # Try to find and highlight the current day
        # Days are formatted as either " D" or "DD" (right-aligned in 3-char fields including space)
        import re
        
        # Pattern to match day numbers (with surrounding spaces)
        # We need to preserve alignment, so we'll replace while keeping spacing
        day_str_1 = f' {current_day} '  # single digit with spaces
        day_str_2 = f' {current_day:2d} '  # right-aligned in 3-char field
        
        if current_day < 10:
            # Single digit: look for " D " pattern
            pattern = f' {current_day} '
            if pattern in modified_line:
                highlighted = f'\033[7m {current_day}\033[0m '
                modified_line = modified_line.replace(pattern, highlighted, 1)
        else:
            # Double digit: look for "DD " pattern  
            pattern = f'{current_day} '
            if pattern in modified_line:
                highlighted = f'\033[7m{current_day}\033[0m '
                modified_line = modified_line.replace(pattern, highlighted, 1)
        
        result_lines.append(modified_line)
    
    return '\n'.join(result_lines)


def get_complete_date():
    """Return complete date/time in the format: Mon Jan  5 11:37:49 WET 2026"""
    now = datetime.datetime.now()
    # Get timezone abbreviation
    tz_name = now.strftime('%Z')
    if not tz_name:
        tz_name = 'UTC'
    
    # Format: Day Mon DD HH:MM:SS TZ YYYY
    return now.strftime(f'%a %b %_d %H:%M:%S {tz_name} %Y')
