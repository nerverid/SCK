#Everyday Test
import sys
from ..helpers.jsonFileHelper import download_file

def open_file(file_name, mode):
    """Open file"""
    try:
        jsonFileHelper.download_file("python_matiz.json")
        the_file = open(file_name, mode, encoding='utf-8')
    except IOError as e:
        print("File doesn't read", file_name, ". Please create file for quiz\n. ",  e)
        #sys.exit()
    else:
        return the_file

def next_line(the_file):
    """return next formatted string"""
    line = the_file.readline()
    line.replace("/", "\n")
    return line

def next_block(the_file):
    """Return next block of data from file"""
    category = next_line(the_file)
    question = next_line(the_file)
    answers = []
    for i in range(4):
        answers.append(next_line(the_file))
    correct = next_line(the_file)
    if correct:
        correct = correct[0]
        explanation = next_line(the_file)
    return category, question, answers, correct, explanation

def welcome(title):
    """Say hello"""
    print("\nHello!")
    print("\nYou are in Quiz block: ", title)

def start_this():
    try:
        
        trivia_file = open_file("trivia.txt", "r")
        title = next_line(trivia_file)
        welcome(title)
        score = 0
        category, question, answers, correct, explanation = next_block(trivia_file)
        while category:
            # type question on screen
            print(category)
            print(question)
            for i in range(4):
                print("\t", i + 1, "-", answers[i])
            
            # gave answer
            answer = input("Your answer: ")

            # tryied answer
            if answer == correct:
                print("\nYes!", end = " ")
                score += 1
            else:
                print("\nNo", end=" ")
            print(explanation)
            print("Score: ", score, "\n\n")

            # turn to next question
            try:
                category, question, answers, correct, explanation = next_block(trivia_file)
            except:
                return
        trivia_file.close()
    except:
        print("File doesn't read ")
        return
    print("It was last question")
    print("Your score ", score)
