####################
## Author: Andrew ##
##****************##


def get_fuel_material():
    begin_odom = int(input("Please enter your beginning odometer reading: "))
    ending_odom = int(input("Please enter your ending odometer reading: "))
    gallons_to_fill = int(input("Please enter how many gallons to fill your tank: "))
    cost_per_gallong = float(input("Please enter the cost per gallon: "))
    miles_driven_yearly = int(
        input("Please enter the number of miles driven per year: ")
    )
    return (
        begin_odom,
        ending_odom,
        gallons_to_fill,
        cost_per_gallong,
        miles_driven_yearly,
    )


begin, end, gal_to_fill, cost_per_gal, miles_driven = get_fuel_material()

total_distance = end - begin
mpg = float(total_distance / gal_to_fill)
fuel_cost = float(cost_per_gal / mpg)
total_cost_per_year = float(miles_driven * fuel_cost)
print(
    f"Miles Per Gallon: {mpg:.2f}\nFuel Cost Per Mile: ${fuel_cost:.2f}\nTotal Cost Per Year: {total_cost_per_year:.2f}"
)
