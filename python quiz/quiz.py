
'''
make sure that the python file and text files are in a folder

'''
#retrieving random question
import random

#keeps a copy of the question asked
QuestionAsked = []


#storing answer to compare user answer and textfile answer
answer = ""

#users answer
user_ans = ""

#amount of questions asked
i = 0

#score
score = 0

#questions amount
qamount = 10


while i != qamount:
    #getting random number representing random question
    randomQuestion = random.randint(0,19)

    #making sure we don't get a repeated question
    while(randomQuestion in QuestionAsked):
        randomQuestion = random.randint(0,19)

    #opening text file that contains the questions
    q = open("questions.txt")

    #opening text file that contains the answers
    a = open("answers.txt")
        
    #adding the question to an array so that it's not asked again
    QuestionAsked.append(randomQuestion)
        
    #looping through each question in the text file
    for x, line in enumerate(q):
        #x is the line
        if x == randomQuestion:
            #displaying question number and then question
            print(i+1,line)
            break
    q.close()

    #looping through each answer in the text file
    for x, line in enumerate(a):
        #x is the line
        if x == randomQuestion:
            #storing answer to compare with user input
            answer = line
            break
    a.close()

        
    user_ans = input("true false\n")
        
    #testing to see is user answer is same as text document
    #adding one to the user score
    if(user_ans in answer):
        score += 1
            
        
    i+=1

print("you got: ",score,"/",qamount)

            
        
    



