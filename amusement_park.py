age =18
if age < 4:
    print('free of charge')
elif age >= 4 and age < 18:
    print("$5")
else:
    print("$18")

#different way
if age < 4:
    price = "$0"
elif age >= 4 and age <18:
    price = "$5"
else:
 price = "$18"

print("your admission is " + price + ".")