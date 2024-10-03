####################
## Author: Andrew ##
####################

def main():
    elevator = False
    sqft = int(input("Enter the apartment size in: "));
    bedroom = int(input("Enter the number of bedrooms: "));
    bathroom = int(input("Enter the number of bathrooms: "));
    flr = int(input("Enter the floor: "));
    elevator = input("Enter elevator (true or false): ").lower();
    offst_parking = input("Enter off street parking (true or false): ");
    rent = int(input("Enter how much rent: "));

    is_elevator = elevator == 'true';
    is_offst = offst_parking == 'true';


    if (sqft >= 1500 and bedroom >= 2 and bathroom >= 2 and is_elevator and is_offst and rent <= 2000):
        print("Include the apartment under Criteria 1\n");
    if (sqft >= 500 and bedroom == 1 and bathroom == 1 and rent <= 1000):
        print("Include the apartment under Criteria 2\n");
    if (sqft >= 2000 and bedroom == 3 and bathroom == 2 and flr > 4 and is_elevator and rent <= 3000):
        print("Include the apartment under Criteria 3\n");
    if (sqft >= 1500 and bedroom == 3 and bathroom == 2 and flr > 4 and is_elevator and is_offst and rent <= 3000):
        print("Include the apartment under Criteria 4\n");


if __name__ == "__main__":
    main()
