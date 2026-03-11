#!/usr/bin/env python3
"""calendar_gen - Generate text calendars. Zero deps."""
import sys, calendar, datetime

def main():
    now = datetime.date.today()
    year = now.year
    month = None
    args = sys.argv[1:]
    if args:
        if len(args) == 1: 
            if int(args[0]) > 12: year = int(args[0])
            else: month = int(args[0])
        elif len(args) >= 2:
            year, month = int(args[0]), int(args[1])
    if month:
        print(calendar.month(year, month))
    else:
        print(calendar.calendar(year))

if __name__ == "__main__":
    main()
