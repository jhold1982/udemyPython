print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Child tickets cost $5.00")
    elif age <= 18:
        bill = 7
        print("Youth tickets cost $7.00")
    else:
        bill = 12
        print("Adult tickets cost $12.00")

    wantsPhoto = input("Do you want a photo with your ride? y for Yes, n for No. ")
    if wantsPhoto == "y":
        # Add $3 to bill
        bill += 3

    print(f"Your total ticket price is ${bill}.00")
else:
    print("Sorry you have to grow taller before you can ride.")

# weight = 85
# height = 1.85
#
# bmi = weight / (height ** 2)
#
# if bmi >= 25:
#     print("You fat fuck")
# elif bmi >= 18.5:
#     print("You're normal")
# else:
#     print("Eat a burger.")
#







