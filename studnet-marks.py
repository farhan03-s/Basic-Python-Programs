theory=int(input("Enter theory marks: "))
practicals=int(input("Enter practicals marks: "))
total_marks=theory+practicals
if theory>=35 and practicals>=50 and total_marks>=60:
    print("Student passed the exam")
else:
    print("Student failed the exam")
