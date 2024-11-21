user_input = int(input("Give a number of seconds (intger): "))

seconds = user_input % 60
minutes = (user_input // 60) % 60
hours = user_input // 3600

print(f"This corresponds to: {hours} hours, {minutes} minutes and" +
      f" {seconds} seconds.")
