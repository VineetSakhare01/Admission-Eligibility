
# A university has the following eligibility criteria for admission:

# Marks in Maths >= 65
# Marks in Physics >= 55
# Marks in chemistry >= 50

# Total marks of three subjects >= 180 OR Total marks in maths 
# & physics >= 140

# Write a program that takes marks in three subjects as input & 
# print whether the student is eligible for admission.

# Asking student to enter subject marks
Maths = int(input("Enter your Mathematics Marks: "))
Physics= int(input("Enter your Physics Marks: "))
Chemistry = int(input("Enter your Chemistry Marks: "))

# total marks
total_marks = Maths+Physics+Chemistry
maths_physics_marks = Maths+Physics

# Conditional Statement

if Maths>=65 and Physics>=55:
    if Chemistry>=50:
        if total_marks>=180 or maths_physics_marks>=140:
            print("Congratulations! you are eligible.")
else:
    print("Sorry, you do not match our admission criteria.")
        

