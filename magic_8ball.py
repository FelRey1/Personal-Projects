# a program that will take in a yes or no question from the user
# will give a response
# can take in questions on after another
#can give different responses to same questions
# @author Felix Reyes, 11/24/22
import random

rand_num = random.randint(1,12)
answer = ""
name = " "
name = input("Whats your name? \n")
if(name == "" or name == " "):
      name = "I"
      
#prints a message for the user 
def print_mess(name,question, answer):
  print(str(name) + " asked " + str(question))
  print("Magic 8-ball's answer: " + str(answer))
      
#prompts the user what question they would like to ask
#checks for blanks, and reprompts if so
def quest():
  question = input("Whats your yes or no Question? \n")
  if(question == "" or question == " "):
        print("No question has been answered \n")
        print("try again\n")
        question = input("What's your yes or no question? \n")
        quest()
  return question

#@return the asnwer based on a random number
def ans(rand_num):     
  if(rand_num == 1):
    answer = "Yes- definitely"

  elif(rand_num == 2):
    answer = "It is decidedly so"

  elif(rand_num == 3):
    answer = "Without a doubt"

  elif(rand_num == 4):
    answer = "Relpy hazy, try again"

  elif(rand_num == 5):
    answer = "Ask again later"
    
  elif(rand_num == 6):
    answer = "better not tell you now"

  elif(rand_num == 7):
    answer = "My sources say no"

  elif(rand_num == 8):
     answer = "Outlook not so good"

  elif(rand_num == 9):
    answer = "Very Doubtful"

  elif(rand_num == 10):
    answer = "yes"

  elif(rand_num == 11):
    answer = "no"

  elif(rand_num == 12):
    answer = "ask again"
       
  else:
    answer = "Error" 
  return answer

question = quest()
answer = ans(rand_num)

#@returns another answer if previous 
#answer is "ask again"
def ask_ag(answer,question):
  if answer == "ask again":
    print_mess(name,question,answer)
    rand = random.randint(1,12)
    question = quest()
    answer = ans(rand)
    ask_ag(answer,question)
    return answer
  elif answer != "ask again":
    rand = random.randint(1,12)
    answer = ans(rand)
  return answer
  
if answer == "ask again":
 answer = ask_ag(answer,question)
print_mess(name,question,answer)

#continues program if the user wants to ask another question
def cont():
  con = input("want to ask another question? y or n \n")
  if con == 'y':
    question = quest()
    rand_num = random.randint(1,12)
    answer = ans(rand_num)
    ask_ag(answer,question)
    print_mess(name,question,answer)
    cont()
  elif con == 'n':
    print("Goodbye!")
  else:
    print("please enter y or n")
    cont()

cont()
