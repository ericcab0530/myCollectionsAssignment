#gradebook using lists
#finding letter average using a function
def gradeLetter(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

#input student name for user input
enterName = input("Enter name: ")

#input the grades for user input
grade1 = int(input("Enter first grade: "))
grade2 = int(input("Enter second grade: "))
grade3 = int(input("Enter third grade: "))
grade4 = int(input("Enter fourth grade: "))
grade5 = int(input("Enter fifth grade: "))

#the list of the grades
grades = [grade1, grade2, grade3, grade4, grade5]
#find average by adding them and dividing by length of list
average = sum(grades)  / len(grades)
#store function into a variable
letterGrade = gradeLetter(average)
#print output
print("Student name: ",enterName)
print("The grade average for the list is: ",average)
print("Letter Grade: ",letterGrade)