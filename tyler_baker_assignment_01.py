#Q1 Fix all the syntax and logical errors in the given source code 
#add comments to explain your reasoning

# This program gets three test scores and displays their average.  It congratulates the user if the 
# average is a high score. The high score variable holds the value that is considered a high score.

HIGH_SCORE = 95
 
# Get the test scores.

# I had to turn the input into a float.
# I also decided to add in the variable for test3.
test1 = float(input('Enter the score for test 1: '))
test2 = float(input('Enter the score for test 2: '))
test3 = float(input('Enter the score for test 3: '))

# Calculate the average test score.

#I had to put a parenthesis around the test scores because of PEMDAS.
average = (test1 + test2 + test3) / 3

# Print the average.
print('The average score is ', average)

# If the average is a high score,
# congratulate the user.

# high_score needed to be changed to HIGH_SCORE because high_score is not a defined variable.
if average >= HIGH_SCORE:
    print('Congratulations!')
print('That is a great average!')

#Q2
#The area of a rectangle is the rectangle’s length times its width.
# Write a program that asks for the length and width of two rectangles,
# and prints to the user the area of both rectangles.

# Take the width and length of each respective rectangle.
rectangle_one_width = float(input('Enter the width of the first rectangle: '))
rectangle_one_length = float(input('Enter the length of the first rectangle: '))
rectangle_two_width = float(input('Enter the width of the second rectangle: '))
rectangle_two_length = float(input('Enter the length of the second rectangle: '))

# Find the area of each rectangle
rectangle_one_area = rectangle_one_width * rectangle_one_length
rectangle_two_area = rectangle_two_width * rectangle_two_length

# Print the areas.
print('The area of the first rectangle is ', rectangle_one_area)
print('The area of the second rectangle is ', rectangle_two_area)

#Q3 
#Ask a user to enter their first name and their age and assign it to the variables name and age. 
#The variable name should be a string and the variable age should be an int.  

name = str(input('What is your name? '))
age = int(input('What is your age? '))

#Using the variables name and age, print a message to the user stating something along the lines of:
# "Happy birthday, name!  You are age years old today!"

msg = f'Happy birthday, {name}! You are {age} years old today!'
print(msg)