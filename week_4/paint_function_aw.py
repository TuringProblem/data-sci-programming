####################
## Author: Andrew ##
##****************##
## func_calc_amt_paint
##


from math import ceil


def clac_amt_paint(
    width: float, length: float, height: float, num_doors: int, num_windows: int
) -> float:
    wall_area = 2 * (width * height) + 2 * (length * height)
    door_area = num_doors * 18
    window_area = num_windows * 12
    paintable_area = wall_area - door_area - window_area
    gallons = paintable_area / 400
    return gallons


width = float(input("Please enter the width: "))
length = float(input("Please enter the length: "))
height = float(input("Please enter the height: "))
doors = int(input("Please enter the number of doors: "))
windows = int(input("Please enter the number of windows: "))
total_gallons = clac_amt_paint(width, length, height, doors, windows)
print(ceil(total_gallons))
