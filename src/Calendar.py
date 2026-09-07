#Python Project 3: Display a calendar for a given month and year, highlighting a specific day

import calendar

year = int(input("Enter year: "))
month = int(input("Enter month: "))
day = int(input("Enter day: "))

string = calendar.month(year, month)

highlight = "\033[30;43m"  # Black text on yellow background]"

target_day_with_space = f" {day:2d} "

if target_day_with_space in string:
    highlighted_string = string.replace(target_day_with_space, f"{highlight}{target_day_with_space}\033[0m")
    print(highlighted_string)