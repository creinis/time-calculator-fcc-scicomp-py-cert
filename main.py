
def add_time(start, duration, day_of_week=None):
    # Convert start time to minutes
    start_hour, start_minute = map(int, start[:-3].split(':'))
    if start[-2:] == 'PM':
        start_hour += 12
    start_minutes = start_hour * 60 + start_minute
    
    # Convert duration to minutes
    duration_hour, duration_minute = map(int, duration.split(':'))
    duration_minutes = duration_hour * 60 + duration_minute
    
    # Calculate the end time in minutes and convert back to hour and minutes
    end_minutes = start_minutes + duration_minutes
    end_hour, end_minute = divmod(end_minutes, 60)
    end_hour %= 24
    


# Examples
print(add_time("3:00 PM", "3:10"))
print(add_time("11:30 AM", "2:32", "Monday"))
print(add_time("11:43 AM", "00:20"))
print(add_time("10:10 PM", "3:30"))
print(add_time("11:43 PM", "24:20", "tueSday"))
print(add_time("6:30 PM", "205:12"))

print(add_time("11:06 PM", "2:02"))
print(add_time("11:59 PM", "24:05"))
print(add_time("2:59 AM", "24:00"))
print(add_time("8:16 PM", "466:02"))