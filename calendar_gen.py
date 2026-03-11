#!/usr/bin/env python3
"""Calendar generator — print monthly/yearly calendars."""
import sys, calendar
if __name__ == "__main__":
    if len(sys.argv) == 1:
        import datetime; now = datetime.date.today()
        print(calendar.month(now.year, now.month))
    elif len(sys.argv) == 2:
        print(calendar.calendar(int(sys.argv[1])))
    else:
        print(calendar.month(int(sys.argv[1]), int(sys.argv[2])))
