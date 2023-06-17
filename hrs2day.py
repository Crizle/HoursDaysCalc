def days_in_hours(hours):
  """
  Calculates the number of days in the specified number of hours.

  Args:
    hours: The number of hours to calculate the number of days for.

  Returns:
    The number of days in the specified number of hours.
  """

  hours_in_day = 24
  days = hours / hours_in_day
  return days

def hours_in_days(days):
  """
  Calculates the number of hours in the specified number of days.

  Args:
    days: The number of days to calculate the number of hours for.

  Returns:
    The number of hours in the specified number of days.
  """

  hours_in_day = 24
  hours = days * hours_in_day
  return hours

def main():
  """
  Gets the user's input and calculates the number of hours or days.
  """

  choice = input("Would you like to calculate the number of hours in days "
                 "or the number of days in hours? (h/d): ")

  if choice == "h":
    hours = int(input("Enter the number of hours: "))
    days = days_in_hours(hours)
    print(f"There are {days} days in {hours} hours.")
  elif choice == "d":
    days = int(input("Enter the number of days: "))
    hours = hours_in_days(days)
    print(f"There are {hours} hours in {days} days.")
  else:
    print("Invalid choice.")

if __name__ == "__main__":
  main()

