####################
## Author: Andrew 
##****************
## military time between {0000-1259 -> 1359-2359}
##  


class Airline:
    rating = ['A', 'B', 'C', 'D', 'E', 'F']; 

    def something(self):

    @staticmethod
    def handle_actual(time: int, rate: int):
        if time < 0 or time > 2359:
            rate = 0
        if rate == 0:
            print("Rate: Invalid time entered")

    @staticmethod 
    def hande_time(time: int, rate: int):
        if time < 0 or time > 2359:
            rate = 0
        if rate == 0:
            return Airline.handle_actual(time, rate)
    

    time = int(input("Please enter the scheduled arrival time: "));
    hande_time(time, 1)
    actual_time = int(input("Please enter the actual arrival time: "));
    number = abs(actual_time - time);
    if number == 0:
        print(f"Rating is: {rating[0]}");
    if number > 0 and number <= 15:
        print(f"Rating is: {rating[1]}")
    elif number > 15 and number <= 30:
        print(f"Rating is: {rating[2]}")
    elif number > 30 and number <= 30:
        print(f"Rating is: {rating[3]}")
    elif number > 45 and number <= 60:
        print(f"Rating is: {rating[4]}")
    elif number > 60:
        print(f"Rating is: {rating[5]}")
