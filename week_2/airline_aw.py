####################
## Author: Andrew ##
####################


class Airline:
    ## Making a staticmethod so I do have to use self, as a parameter (making this a fixed func)
    @staticmethod
    def handle_actual(time: int, rate: int):
        if rate == 1:
            rating = ["A", "B", "C", "D", "E", "F"]
            actual_time = int(input("Please enter the actual arrival time: "))
            minutes = actual_time % 100
            if actual_time < 0 or actual_time > 2359 or minutes > 59:
                Airline.handle_actual(time, 0)
            else:

                number = abs(actual_time - time)

                if number == 0:
                    print(f"Rating is: {rating[0]}")
                if 0 < number <= 15:
                    print(f"Rating is: {rating[1]}")
                elif 15 < number <= 30:
                    print(f"Rating is: {rating[2]}")
                elif 30 < number <= 45:
                    print(f"Rating is: {rating[3]}")
                elif 45 < number <= 60:
                    print(f"Rating is: {rating[4]}")
                elif number > 60:
                    print(f"Rating is: {rating[5]}")
        elif rate == 2:
            actual_time = int(input("Please enter the actual arrival time: "))
            print("Invalid time entered.\n")
        elif rate == 0:
            print("Invalid time entered.\n")

    ## defines a method that is bound to the class and not the instance.
    @classmethod
    def handle_time(cls, rate: int):
        if rate == 1:
            time = int(input("Please enter the scheduled arrival time: "))
            minutes = time % 100
            if time < 0 or time > 2359 or minutes > 59:
                Airline.handle_actual(time, 2)
            else:
                Airline.handle_actual(time, 1)


def main():
    obj = Airline()
    obj.handle_time(1)


if __name__ == "__main__":
    main()
