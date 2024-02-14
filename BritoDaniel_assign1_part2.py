#Daniel Brito, Sept 11, 2022, Prof. Khye
#Class Score Demonstrator Code

#Name Variables with test scores for three exams
test_score_1 = 97
test_score_2 = 82
test_score_3 = 85

#Create Variables to store the student's name
student_first_name = "Grace"
student_last_name = "Hopper"

#Assign a value to add bonus points to a score through a variable
bonus_points = 2

#Create a variable containing the name of the class being discussed
class_name = "'Introduction to Computer Programming' (no prior experience)"

#Print line of asterisks before the title of the class
print("*"*60)

#print the class name
print(class_name)

#Print line of asterisks after the title of the class
print("*"*60)

#print a blank line to separate
print()

#print the students name, with the first name coming after the last separated by a comma
print("Student:",student_last_name+',', student_first_name )

#print the recent test scores that were stored in the variables above, separated as shown in the assignment
print("Most recent test scores:", str(test_score_1)+",",test_score_2,"and",test_score_3)

#create a variable for the average of the scores
average_score=(test_score_1+test_score_2+test_score_3)/3

#print the average score
print("Average score:",average_score)

#print the bonus points, as stored in the variable above
print("Class bonus points:",bonus_points)

#print the average score with the bonus points added, using variables and not literals
print("Average score with bonus points added:",average_score+bonus_points)
