Loop = True
Loop_2 = True
while Loop == True:
    Base = input("Enter Triangle Base in whole numbers: ")
    if Base.isnumeric():
        Height = input("Enter Triangle Height in whole numbers: ")
        Loop = False
    else:
        print("Error enter whole number only.")
