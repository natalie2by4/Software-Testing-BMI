
#converting height strictly to inches
def heightConversion(feet, inches):
    feet = float(feet)
    inches = float(inches)
    height = (feet * 12) + inches
    return height
    
#calculating the Body Mass Index    
def BMI_Calc(weight, height):
    weight = float(weight)
    
    weight = weight * 0.45
    height = height * 0.025
    height = height * height
    bmi = weight / height
    bmi = round(bmi, 1)
    
    return bmi

#results of the bmi values
def results(bmi):
    if bmi <= 18.5:
        result = "Underweight"
    elif bmi >= 18.4 and bmi <= 24.8:
        result = "Normal Weight"
    elif bmi >= 25 and bmi <= 29.9:
        result = "Overweight"
    else:
        result = "Obese"
    
    return result

#main
print("\n")
print("Welcome to the Body Mass Index Calculator! \n")

#input
feet = input("Enter your height in feet: ")
inches = input("Enter the remaining inches to your height: ")
weight = input("Enter your weight in pounds: ")
print("\n")

height = heightConversion(feet, inches)
BMI = BMI_Calc(weight, height)
results = results(BMI)

print("Body Mass Index: {}, {}".format(BMI, results))










