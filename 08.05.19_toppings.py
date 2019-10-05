requested_toppings = ['mushroons', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    print("adding " + requested_topping +".")
print("\nFinished making your pizza!")

#if the pizzeria running out of green peppers
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("sorry we are running out of green pepper right now")
    else:
        print("Adding " + requested_topping +".")
print("\nFinished making pizza!")

#checking that a list is not empty
#sample is if empty means customer wants a plain pizza

requested_toppings = []
if requested_toppings:  #behaviour when there is a list
    for requested_topping in requested_toppings:
        print("adding " + requested_topping + ".")
    print("\nFinished making your pizza!")
else: #behavious when there is not list inside
    print("are you sure you want a plain pizza?")