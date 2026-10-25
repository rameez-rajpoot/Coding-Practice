def get_marks(subject):
    while True:
      marks = int(input(f"Enter marks for {subject}: "))
      if 0 <= marks <=100:
        return marks
      else:
        print("Enter marks b/w (0 - 100)")

def calc_grade(percentage):
    if percentage >= 90:
        return 'A+'
    elif percentage >= 80:
        return 'A'
    elif percentage >= 70:
        return 'B'
    elif percentage >= 60:
        return 'C'
    else:
        return 'D'
    
name = input("Enter Student name : ")
subjects = [
    "English",
    "Islamiyat",
    "Computer",
    "Physics",
    "Mathematics"
]

marks = []

for subject in subjects:
    marks.append(get_marks(subject))

obtain_marks = sum(marks)
percentage = obtain_marks/500*100
grade = calc_grade(percentage)

print(subjects)

print("____Student Card____")
print("Student name :",name)
print("Student total marks :",obtain_marks,"/ 500")
print("Percentage :",percentage)
print("Grade :",grade)