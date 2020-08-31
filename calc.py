Loop = True
Loop_2 = True
while Loop == True:
    Base = input("Enter Triangle Base in whole numbers: ")
    if Base.isnumeric():
        Height = input("Enter Triangle Height in whole numbers: ")
        Loop = False
    else:
        print("Error enter whole number only.")
        
while Loop_2 == True:
    if Height.isnumeric():
        Area = int(Base) * int(Height) / 2
        print(f"The area of this triangle is {Area}!")
        Loop_2 = False
    else:
        print("Error enter whole number only")
        Height = input("Enter Triangle Height in whole numbers: ")
