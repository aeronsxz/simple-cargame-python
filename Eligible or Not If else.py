name = input("Please input your name here: ")
age = int(input("Please input your age here: "))
grade = int(input("Please input your grade here: "))

if age >= 18 and age < 22:
    if grade >= 80:
        print('Name: ',name)
        print('Age: ',age)
        print('Grade: ',grade)
        print(f"Hello {name}! Congratulations, you are eligible for the loan")
    else:
        print(f"Sorry {name}, your grade is not eligible for the loan.")
elif age > 23 or grade >= 80:
    print(f"Sorry {name}, your age is not eligible for the loan")
else:
    print("Unknown Input")