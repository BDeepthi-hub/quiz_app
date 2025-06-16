
# Import the required libraries
from colorama import Fore, Style

# For user Name input
name= input("Enter your name: ")

# Define the questions
questions = ( "1. Who developed Python language?: ",
             
             "2. What data type is the result of the expression 5 // 2 in Python?: ",

              "3. What is the primary purpose of the if statement in Python?: ",

             "4.What is the value returned by math.floor(3.4)?: ",

             "5. Which of the following is a mutable data structure in Python?: ",

             "6. What is the correct file extension for Python files?",

             " 7. How do you create a variable in Python?",

              "8. What is the output of the following code? print(type(5))",

             "9.  Which of the following is used to take input from the user in Python?",

              "10.  What is the output of the following code? print(2 ** 3)",

             "11. What is the correct way to write a comment in Python?",

             
              "12.  Which of the following is a mutable data type in Python?",

             "13. How do you start a function definition in Python?",

              "14. What will be the output of the following code? print('Python'[0])",

              "15. Which of the following is NOT a valid Python keyword?"


             )
# Define the options for each question
options = (("A. Dennis Ritchie","B. James Gosling","C. Guido Van Rossum","D. Graham Bell"),
           
           ("A. float","B. integer","C. boolean","D. string"),

           ("A. To execute a block of code based on a condition","B. To perform mathematical operations","C. To repeat a block of code.","D. To define a function"),

           ("A. 3","B. 4","C. 3.0","D. 4.0"),

           ("A. Tuple","B. String","C. List","D. Dictionary"),

           ("A. .pyth","B. .py","C. .pyt","D. .python"),

            ("A. var x = 10","B. x = 10","C. int x = 10","D. dim x = 10"),

            ("A. <class 'int'>","B. <class 'float'>","C. <class 'str'>","D. <class 'list'>"),

            ("A. cin","B. input()","C. get()","D. scan()"),

            ("A. 5","B. 6","C. 8","D. 9"),

            ("A. // This is a comment","B. /* This is a comment */","C. # This is a comment","D. <-- This is a comment -->"),

            ("A. tuple","B. string","C. list","D. int"),

            ("A. function myFunction():","B. def myFunction:","C. def myFunction():","D. fun myFunction():"),

            ("A. Python","B. P","C. h","D. n"),

            ("A. def","B. class","C. if","D. loop")


           )

# Define the correct answers
answers = ("C","B","A","A","C","B","B","A","B","C","C", "C", "C","B","D")

# Initialize variables to keep track of the user's guesses and score
guesses = []
score = 0
question_num = 0

# Loop through each question
for question in questions:
    print(Fore.WHITE +"**************")
    print(Fore.CYAN + question)

# Loop through each option for the current question
    for option in options[question_num]:
        print(option)                                                # Print options
 
# Get the user's guess
    guess = input(Fore.LIGHTMAGENTA_EX +"Enter (A, B, C, D): ").upper()

#Add the user's guess to the list of guesses
    guesses.append(guess)

# Check if the user's guess is correct 
    if guess == answers[question_num]:
        score += 1
        print(Fore.LIGHTGREEN_EX +"CORRECT!!!")                     # Print for correct answer
    else:
        print(Fore.LIGHTRED_EX +"INCORRECT!")                       # Print for incorrect answer
        print(f"{answers[question_num]} is the correct answer")     # Print the correct answer

# Increment the question numbers
    question_num += 1

# Print the results
print(Fore.WHITE +"---------------------")
print(Fore.LIGHTRED_EX + "      RESULTs      ")
print(Fore.WHITE + "---------------------")

# Print the correct answers
print(Style.BRIGHT,Fore.LIGHTGREEN_EX +"Answers: ",end="")
for answer in answers:
    print(answer,end=" ")                                           # Print each answer separated by a space
print()                                                             # Move to the next line

# Print the user's guesses
print(Style.BRIGHT,Fore.LIGHTBLUE_EX +"Guesses: ",end="")
for guess in guesses:
    print(guess,end=" ")                                            # Print each guesses separated by a space
print()                                                             # Move to the next line

# Calculate the user's score as a percentage
score = int(score / len(questions) * 100)
# print the user's score
print(Fore.LIGHTYELLOW_EX + f"Hello! {name} Your score is: {score}%")
