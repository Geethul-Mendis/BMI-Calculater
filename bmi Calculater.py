print("This is your BMI calculator. Let's see what your BMI is.")
 
w = float(input("Weight (in kg): "))
h = float(input("Height (in meters): "))
bmi = w / (h * h)

print("Your BMI is: {:.2f}".format(bmi))