####################
## Author: Andrew ##
##****************##

# $.10 per mile from the shop to the customer location
# 10% for orders <= $50 and 5% for orders > $50
miles_process = lambda a: a * 0.10


def take_your_order():
    order_amount = float(input("Please enter the amount of the order: "))
    percentage = get_discount(order_amount)
    print(f"percentage: %{percentage:.2f}")

    miles_from_shop = int(input("Please enter the miles: "))
    price_miles = miles_process(miles_from_shop)

    print(f"Amount from miles: ${price_miles:.2f}")

    total = order_amount + percentage + price_miles

    print(f"Total To Be Collected: ${total:.2f}")


def get_discount(value: float) -> float:
    if value > 50.0:
        return value * 0.05
    if value <= 50.0:
        return value * 0.10
    else:
        return 0.00


take_your_order()
