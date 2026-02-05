import datetime, bday_messages.py # pyright: ignore[reportMissingImports]

today = datetime.date(2026, 1, 30)

next_birthday = datetime.date(2026, 12, 13)

date1 = today
date2 = next_birthday

days_away = (date2 - date1).days

if today == next_birthday:
    print(bday_messages.bday_messages()) # pyright: ignore[reportUndefinedVariable]
else:
    print(f"My next birthday is {days_away} days away!")
