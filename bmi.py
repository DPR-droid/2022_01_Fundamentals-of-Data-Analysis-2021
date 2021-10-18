# bmi.py
# This program calculate the users BMI
# The inputs are the person's height in centimetres and weight in kilograms.
# The output is their weight divided by their height in metres squared.
# Author David


# Set the weight and hieght to test the calculations
#weight = 65
#height = 180

# Input data from user
weight = int(input("Enter weight: "))
height = int(input("Enter height: "))


# Location of bmi calculation
# https://www.diabetes.ca/managing-my-diabetes/tools---resources/body-mass-index-(bmi)-calculator
# Test calculations 
# bmi = weight / (height * height)
# bmi = weight / ((height * height)/100)
# bmi = weight / ((height * height)/10000)

# Final Calculation two decimal points
bmi = round((weight / ((height * height)/10000)),2)

# Test print 
#print(str(bmi))

# Output to users BMI
print("BMI is " + str(bmi) + ".")