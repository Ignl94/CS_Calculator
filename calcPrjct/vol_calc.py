# I created loop variables to use in my loops.
loop_1 = True
loop_2 = True

# created introduction
print("Welcome to my volume calculator \nEnter inputs to get the area of a cone in centimeters")

# created loop, taking in input and evaluating parameters.
while loop_1 == True:
    radius = input("Enter the radius in whole numbers ")
    if radius.isnumeric():
        height = input("Enter the height in whole numbers ")
        loop_1 = False
    else:
        print("Error please input whole numbers only.")

# created loop, performs volume calculation V=πr<sup>2</sup>h/3 , prints output.
while loop_2 == True:
    if height.isnumeric():
        radius_sq = int(radius) * int(radius)
        height_div = int(height) / 3
        r_h_mult = radius_sq * height_div
        pi_mult = r_h_mult * 3.14
        result = f"The volume of this cone is {pi_mult} centimeters cubed"
        print(result)
        loop_2 = False
    else:
        print("Error please input whole numbers only")
        height = input("Enter the height in whole numbers ")
