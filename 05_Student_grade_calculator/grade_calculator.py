print("""Grading system 
1. A+ (90-100) 
2. A (80-89) 
3. B (70-79) 
4. C (60-69) 
5. D (50-59) 
6. F (0-49)
""")
try:

 maths = float(input("Enter your marks for Maths: "))
 english = float(input("Enter your marks for English: "))
 science = float(input("Enter your marks for Science: "))
 total = maths + english + science 


 percentage = (total /300) * 100

 if (
    maths < 0 or maths > 100 or
    english < 0 or english > 100 or
    science < 0 or science > 100

 ):
    print("Invalid marks entered. Please enter marks between 0 and 100.")

 elif percentage >= 90:
    print("Your grade is A+")

 elif percentage >= 80:
    print("Your grade is A")

 elif percentage >= 70:
    print("Your grade is B")

 elif percentage >= 60:  
    print("Your grade is C")

 elif percentage >= 50:  
    print("Your grade is D")

 else:

    print("Your grade is F")

except KeyboardInterrupt:
    print("Operation cancelled by user")
except ValueError:
    print("Invalid input. Please enter numeric values for marks.")