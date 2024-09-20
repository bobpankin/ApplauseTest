from datetime import datetime

def days_until_birthday(birthday):
    today = datetime.now()
    current_year = today.year

    # Create a birthday date for this year
    birthday_this_year = birthday.replace(year=current_year)

    # Check if the birthday has already passed this year
    if today > birthday_this_year:
        # If so, set birthday to next year
        birthday_next_year = birthday.replace(year=current_year + 1)
        return (birthday_next_year - today).days
    else:
        # If the birthday is yet to come this year
        return (birthday_this_year - today).days

if __name__ == "__main__":
    # Input your birthday (format: YYYY-MM-DD)
    birthday_input = input("Enter your birthday (YYYY-MM-DD): ")
    birthday = datetime.strptime(birthday_input, "%Y-%m-%d")
    
    days_remaining = days_until_birthday(birthday)
    print(f"There are {days_remaining} days until your next birthday!")
