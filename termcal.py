#!/usr/bin/env python3
import os
import json
import calendar
import argparse
from datetime import datetime, timedelta

# ANSI colors
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RESET = '\033[0m'

NOTES_PATH = os.path.expanduser("~/.termcal/notes.json")


def load_notes():
    if not os.path.exists(NOTES_PATH):
        os.makedirs(os.path.dirname(NOTES_PATH), exist_ok=True)
        with open(NOTES_PATH, 'w') as f:
            json.dump({}, f)
    with open(NOTES_PATH, 'r') as f:
        return json.load(f)


def save_notes(notes):
    with open(NOTES_PATH, 'w') as f:
        json.dump(notes, f, indent=2)


def format_day(day, today, year, month, notes):
    if day == 0:
        return "  "
    date_str = f"{year}-{month:02d}-{day:02d}"
    if today.year == year and today.month == month and today.day == day:
        return f"{RED}{day:2d}{RESET}"
    return f"{day:2d}"


def print_calendar(year, month, notes):
    today = datetime.today()
    calendar.setfirstweekday(calendar.MONDAY)
    month_matrix = calendar.monthcalendar(year, month)
    month_name = calendar.month_name[month]

    print(f"\n     {month_name} {year}")
    print("Mo Tu We Th Fr Sa Su")
    for week in month_matrix:
        line = ""
        for day in week:
            day_str = format_day(day, today, year, month, notes)
            line += f"{day_str} "
        print(line.rstrip())

    
    shown_notes = [k for k in notes if k.startswith(f"{year}-{month:02d}")]
    if shown_notes:
        print(f"\n{YELLOW}Notes:{RESET}")
        for date_str in sorted(shown_notes):
            day = int(date_str[-2:])
            print(f"{day:2d}: {notes[date_str]}")

    # Info about today
    if today.year == year and today.month == month:
        print(f"\nToday: {GREEN}{today.day} {month_name} {year}{RESET}\n")


def add_note(date_str, text):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        print("Error: Invalid date format. Use YYYY-MM-DD.")
        return
    notes = load_notes()
    notes[date_str] = text
    save_notes(notes)
    print(f"Note added on {date_str}: {text}")


def delete_note(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        print("Error: Invalid date format. Use YYYY-MM-DD.")
        return
    notes = load_notes()
    if date_str in notes:
        del notes[date_str]
        save_notes(notes)
        print(f"Note deleted for {date_str}.")
    else:
        print(f"No note found for {date_str}.")


def list_notes():
    notes = load_notes()
    if not notes:
        print("No notes found.")
        return
    print(f"{YELLOW}All notes:{RESET}")
    for date in sorted(notes.keys()):
        print(f"{date}: {notes[date]}")


def main():
    parser = argparse.ArgumentParser(description="Aesthetic terminal calendar (no dependencies)")
    parser.add_argument("--year", type=int, help="Year to show")
    parser.add_argument("--month", type=int, help="Month to show")
    parser.add_argument("--next", action="store_true", help="Show next month")
    parser.add_argument("--prev", action="store_true", help="Show previous month")
    parser.add_argument("--add", nargs=2, metavar=('YYYY-MM-DD', 'TEXT'), help="Add a note to a date")
    parser.add_argument("--delete", metavar='YYYY-MM-DD', help="Delete note by date")
    parser.add_argument("--list", action="store_true", help="List all notes")

    args = parser.parse_args()
    today = datetime.today()

    if args.add:
        add_note(args.add[0], args.add[1])
        return

    if args.delete:
        delete_note(args.delete)
        return

    if args.list:
        list_notes()
        return


    year = args.year or today.year
    month = args.month or today.month

    if args.next:
        dt = datetime(year, month, 15) + timedelta(days=31)
        year, month = dt.year, dt.month
    elif args.prev:
        dt = datetime(year, month, 15) - timedelta(days=31)
        year, month = dt.year, dt.month

    notes = load_notes()
    print_calendar(year, month, notes)


if __name__ == "__main__":
    main()
