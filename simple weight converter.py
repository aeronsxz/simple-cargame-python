weight = float(input("Please input your weight here: "))
ask = input("Please select if the input weight is in L = LBS or K = KG ")

if ask.lower() == "k":
    conversion_KG_LBS = weight / 0.45
    print(f"You are {conversion_KG_LBS} in pounds.")

elif ask.lower() == "l":
    conversion_LBS_KG = weight * 0.45
    print(f"You are {conversion_LBS_KG} in kilograms")

else:
    print("Selection Error")