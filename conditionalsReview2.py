#Create a Python script that assigns a grade to a student based on their exam score.
score=int(input("Enter your score:"))


if score >= 90:
    print("your score is an A")
   
elif score >= 80 and score < 90:
    print(" your score is a B")

elif score>=70 and score < 80:
    print("your score is a C")

elif score>=60 and score <70:
    print("your score is a D")

elif score>=50 and score <60:
 print("your score is a F")