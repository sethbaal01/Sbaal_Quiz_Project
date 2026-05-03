# Name: Seth Baal
# Class 

#When building new quizzes, refer to the formatting guidlines at the top of the defualt 'quiz.txt' file

import os
from colorama import Fore, Style, init
init(autoreset=True)

#This function handes actually reading the files and 
def loadQuestions(filePath):
    questions = []
    
    with open(filePath, 'r', encoding='utf-8') as file: #utf-8 encoding ensures cross-platform handling of data translation
        for line in file:
            line = line.strip()
            
            # Skip empty lines and comments
            if not line or line.startswith('#'):
                continue
            
            # Validate format
            if '|' not in line:
                print(f"Skipping malformed line: {line}")
                continue
            
            # Split only on the first '|'
            question, answer = line.split('|', 1)
            
            questions.append((question.strip(), answer.strip()))
    
    return questions

#This function is in charge of running the quiz and handling user input.
def runQuiz(questions):
    score = 0
    
    for i, (question, answer) in enumerate(questions, start=1):
        print(Style.BRIGHT + Fore.BLUE + f"\nQuestion {i}: {question}")
        userAnswer = input("Your answer: ").strip()
        
        if userAnswer.lower() == answer.lower(): #.lower() handles caps checking
            print(Fore.GREEN + "Correct!")
            score += 1
        else:
            print(Style.BRIGHT + Fore.RED + f"Incorrect!\nCorrect answer: {answer}")
    
    return score

#This is the main function, just calling this runs the whole thing
def main():

    defaultPath = "quiz.txt"
    userPath = input(f"Enter a File path for quiz (Press enter for default quiz: {defaultPath}): ")
    
    # Decide which path to use
    if not userPath:
        filePath = defaultPath #this is a 'cheat' way of avoiding recording key presses I guess
    elif os.path.exists(userPath):
        filePath = userPath
    else:
        print("File not found. Using default quiz.") #default also used if file path was not found
        filePath = defaultPath
    
    questions = loadQuestions(filePath)
    
    if not questions:
        print("No valid questions found.")
        return
    
    print("Quiz Start: ")
    
    score = runQuiz(questions)
    
    total = len(questions)
    percentage = (score / total) * 100
    
    print(Fore.CYAN + "\nResults:")
    print(Fore.CYAN + f"Score: {score}/{total}")
    print(Fore.CYAN + f"Percentage: {percentage:.2f}%")
    

if __name__ == "__main__":
    main()
