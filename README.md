# yday

Simple tool that prints the current day of the year.

Version: 0.1.2

## Usage

```bash
python app/main.py           # Print day of year
python app/main.py -w        # Print week of year
python app/main.py -n        # Print day name (localized)
python app/main.py -m        # Print calendar for current month (highlights today)
python app/main.py -c        # Print complete date/time
python app/main.py --version
python app/main.py --help
```

Example output:
```
$ python app/main.py
5

$ python app/main.py -w
1

$ python app/main.py -n
monday

$ python app/main.py -m
   January 2026
Su Mo Tu We Th Fr Sa
          1  2  3  4
 5  6  7  8  9 10 11    # Current day (5) is highlighted
12 13 14 15 16 17 18
19 20 21 22 23 24 25
26 27 28 29 30 31

$ python app/main.py -c
Mon Jan  5 11:37:49 WET 2026
```

## Tests

```bash
python test/test_main.py
```
