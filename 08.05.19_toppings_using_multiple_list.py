available_toppings = ['mushroom', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushroom', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("add " + requested_topping + ".")
    else:
        print("sorry, we don't have" + requested_topping + ".")
print("\nFinish making your pizza!")