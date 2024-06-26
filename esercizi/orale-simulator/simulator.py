# questo programma python prende in input 2 file [question, answer] 
# ogni domanda/risposta inizia con un "#"

import random
import sys
import os

class QandA: 
    question = ""
    answer = ""

def getAllRecord(fileToRead):
    doc = ""
    with open(fileToRead, "r") as file:
      doc = file.read()

    # le domande sono del formato # domanda ... fine riga
    question = []
    rec = ""
    toRec = False
    for i in range(0, len(doc)-1):
      if(doc[i] == "#"):
        question.append(rec)
        rec = ""

      if(doc[i] == "\t"):
        rec += " "
      else: 
        rec += doc[i]
      
    question.pop(0)
    return question

def main():

  if(len(sys.argv) <= 1):
    print("ERR usage: python3 QandA.py [question.txt] [answer.txt]")
    return 1
  elif(len(sys.argv) == 2):
    answerMode = False
  else:
    answerMode = True

  print(answerMode)

  question = getAllRecord(sys.argv[1])

  if(answerMode):
    answer = getAllRecord(sys.argv[2])

  qa = []

  if(answerMode): 
    for i in range (0, min(len(question), len(answer))):
      qaObj = QandA()
      qaObj.question = question[i]
      qaObj.answer = answer[i]
      qa.append(qaObj)
  else:
    for i in range (0, len(question)):
      qaObj = QandA()
      qaObj.question = question[i]
      qa.append(qaObj)

  action = False

  while True:   

    if(not action):  
      i = random.randint(0,len(qa)-1)
      print(qa[i].question)

    choice = input()

    action = True

    if(choice == "q"): #QUIT
      break
    elif(choice == "a" and answerMode): #ANSWER
      print(qa[i].answer)
    elif(choice == "c"): #CLEAR
      os.system('clear')
      print(qa[i].question)
    elif(choice == "p"): #PREVIOUS
      if(i-1 >= 0):
        i = i - 1
      os.system('clear')
      print(qa[i].question)
    elif(choice == "n"): #NEXT
      if(i+1 < len(question)):
        i = i + 1
      os.system('clear')
      print(qa[i].question)
    elif(choice == "help"): # OPTIONS
      print("\n- q => quit\n- c => clear prompt\n- p => previous question\n- n => next question\n- a => (IF ANSWER MODE) print answer\n")
    else:
      action = False

        

if __name__ == '__main__':
    # This code won't run if this file is imported.
    main()
