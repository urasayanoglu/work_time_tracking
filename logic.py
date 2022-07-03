""" Basic logic for the work time tracking!"""
import datetime 

MIN_TIME_AT_WORK = 750 # Minimum time (in minutes) a worker should be working daily
WEEKLY_WORK_TIME = 3750 # Required work time in minutes in a week
DAYS_IN_A_WEEK = {1: "monday", 2: "tuesday", 3: "wednesday", 4: "thursday", 5: "friday", 6: "saturday", 7: "sunday"}

status = True

while status:
    print("-" * 25)
    print("(1): Start of the day")
    print("(2): Give a break")
    print("(3): Return to work ")
    print("(4): End of the day!")
    user_input = input("Please type the number corresponding to your decision: ")
    
    my_date = datetime.date.today() 
    year, week_num, day_of_week = my_date.isocalendar()

    if int(user_input) == 1:
        print("Good morning, I wish you a nice and an easy day!")
        with open("work_time_tracking.txt", "a") as tt_document:
            tt_document.write(f'Week No: {week_num}, {my_date.strftime("%d-%m-%y")}, {DAYS_IN_A_WEEK[day_of_week].capitalize()}')
        

    elif int(user_input) == 2:
        print("You are in a break now!")
    elif int(user_input) == 3:
        print("Your break has ended and now you're back for work!")
    elif int(user_input) == 4:
        print("It's time to call it a day, enjoy rest of the day.")
        status = False


