import datetime

current_date = datetime.date.today()
time = datetime.datetime.now().time()

def display_current_datetime():
    current_time = time.strftime("%H:%M:%S")
    
    print("Current date & time:", current_date, current_time)

display_current_datetime()



def calculate_future_date(days):
        time_delta = datetime.timedelta(days=days)
        future_date = current_date + time_delta

        print("Future date:",future_date)

days = int(input("Enter the number of days to add to the current date:"))

calculate_future_date(days)