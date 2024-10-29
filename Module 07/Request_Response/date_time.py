from datetime import datetime

# current = datetime.datetime.now()
# print(current.year)

# format_current = current.strftime("%B %d, %Y")
# format_current = current.strftime("%d/%m/%Y")
# print(format_current)

# date difference
date1 = datetime(1983, 1, 1)
# date2 = datetime.datetime(2024, 9, 30)
#
# diff = (date2 - date1)
# print(diff)
def add_months(current_date, months_to_add):
    new_date = datetime(current_date.year + (current_date.month + months_to_add - 1) // 12,
                        (current_date.month + months_to_add - 1) % 12 + 1,
                        current_date.day, current_date.hour, current_date.minute, current_date.second)
    return new_date

new_date = add_months(date1, 5)
print(new_date)