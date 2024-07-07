from datetime import datetime

time = datetime.datetime.now().time()

now = datetime.datetime.now()

def display_current_datetime():   
    current_date = datetime.date.today()


current_datetime = now.strftime("%d-%m-%Y %H:%M:%S")    
print("Current date & time:", current_datetime)


def calculate_future_date(days):
        time_delta = datetime.timedelta(days=days)
        current_date = datetime.date.today()
        future_date = current_date + time_delta

        print("Future date:",future_date)

days = int(input("Enter the number of days to add to the current date:"))

calculate_future_date(days)