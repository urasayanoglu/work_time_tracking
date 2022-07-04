""" Basic logic for the work time tracking!"""
import datetime 

MIN_TIME_AT_WORK = datetime.timedelta(seconds=26100) # Minimum time (in seconds) a worker should be working daily (435 min = 7 hours 15 mins)
WEEKLY_WORK_TIME = datetime.timedelta(seconds=130500) # Required work time (in seconds) in a week (2175 mins = 36 hours 15 mins)
DAYS_IN_A_WEEK = {1: "monday", 2: "tuesday", 3: "wednesday", 4: "thursday", 5: "friday", 6: "saturday", 7: "sunday"}

def seconds_to_hms(totalseconds):
    total_hours = totalseconds // 3600
    total_minutes = (totalseconds - (total_hours * 3600)) // 60
    total_seconds = totalseconds - (total_hours * 3600) - (total_minutes * 60) 
    return f"{total_hours}:{total_minutes}:{total_seconds}"

status = True
number_of_breaks = 0
break_times = []
hours_spent_working = datetime.timedelta(seconds=0)

while status:
    print("-" * 60)
    print("(1): Start of the day")
    print("(2): Give a break")
    print("(3): Return to work ")
    print("(4): End of the day!")
    user_input = input("Please type in the corresponding number to your decision: ")
    
    my_date = datetime.date.today() 
    year, week_num, day_of_week = my_date.isocalendar()
   

    if int(user_input) == 1:
        print("Good morning, I wish you a nice and an easy day!")
        work_day_start_time = datetime.datetime.now()
        with open("work_time_tracking.txt", "a") as tt_document:
            tt_document.write("------------------------------------------------------------\n")
            tt_document.write(f'''Week No: {week_num}, {my_date.strftime("%d-%m-%Y")}, {DAYS_IN_A_WEEK[day_of_week].capitalize()}\n''')
            tt_document.write(f'''Work Day started at {work_day_start_time.strftime("%H:%M:%S")}\n''')
        

    elif int(user_input) == 2:
        print("You are in a break now!")
        break_time = datetime.datetime.now()
        number_of_breaks += 1
        working_hours = break_time - work_day_start_time
        hours_spent_working += working_hours
        break_times.append(break_time.strftime("%H:%M:%S"))
        with open("work_time_tracking.txt", "a") as tt_document:
            tt_document.write(f'''Break started at {break_time.strftime("%H:%M:%S")}\n''')
            tt_document.write(f'''Amount of time you worked till your break: {working_hours}\n''')

    elif int(user_input) == 3:
        print("Your break has ended and now you're back for work!")
        return_to_work = datetime.datetime.now()
        work_day_start_time = return_to_work
        elapsed_time = return_to_work - break_time
        with open("work_time_tracking.txt", "a") as tt_document: 
            tt_document.write(f'''Break ended at {return_to_work.strftime("%H:%M:%S")}\n''')
            tt_document.write(f'''Amount of time passed during your break: {elapsed_time.total_seconds()}\n''')

    elif int(user_input) == 4:
        print("It's time to call it a day, enjoy rest of the day.")
        end_of_day = datetime.datetime.now()
        overtime = hours_spent_working - MIN_TIME_AT_WORK
        with open("work_time_tracking.txt", "a") as tt_document:
            tt_document.write(f'''Work day ended at {end_of_day.strftime("%H:%M:%S")}\n''')
        with open("work_time_daily_summary.txt", "a") as ds_document: 
            ds_document.write(f'''Summary for {my_date.strftime("%d-%m-%Y")} {DAYS_IN_A_WEEK[day_of_week].capitalize()}\n''')
            ds_document.write(f'''Number of breaks: {number_of_breaks}, Total hours worked:{hours_spent_working} Overtime: {overtime} \n''')
            ds_document.write("--------------------------------------------------\n")
        status = False


