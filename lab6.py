



"""
To start, we will generate a random integer between 1 and 20, and 
based on the result of the random number, we check to see if it falls under certain range
if the number is greater than 15, then the result will be "Cherries"
other wise if the number is > 10, then the result will be "Orange"
otherwise if the number is > 5 , then the result will be "Plum"
otherwise if the number is > 2 , then the result will be "Melon"
otherwise if the number is > 1, then the result will be "Bell"
if the number is not any of the above, then the result will be "Bar"


we iterate over using a loop three times and print the results to the user. As an example "Plum Cherries Melon"
"""

"""
num = generate random number 
 
if num is greater than 15, 
 then the result will be "Cherries"
otherwise if the number is > 10, 
  then the result will be "Orange"
otherwise if the number is > 5 , 
  then the result will be "Plum"
otherwise if the number is > 2 , 
  then the result will be "Melon"
otherwise if the number is > 1, 
  then the result will be "Bell"
otherwise
  the result will be "Bar"

loop three times
  print the output (fruit) to the user

"""

import random 

total_earned = 0

def main():
  results = [1]
  for i in range (0,3):
    results.append(spin())

  print ("results", results)
  winner = jackpot(results)

  if(winner):
   print("Winner! you win")
  else:
    print("sorry try again")

  total = count(results)
  option = input("play again? ")
  if option.lower() == "y" or option.lower == "yes" :

def spin()
 rand_num = random.randint(1, 20)
  output = ""
  if (rand_num > 15): 
    output = "Cherries"
  elif(rand_num > 10):
    output = "Orange"
  elif(rand_num > 5):
    output = "Plum"
  elif(rand_num > 2):
    output = "Melon"
  elif(rand_num > 1):
    output = "Bell"
  else:
    output = "Bar"

  print (output, end= "")

def jackpot(results):
  return results[0] == results [1] == results [2]

def count(results):
  total = 0
  money_dict = {
    "Cherries": 1,
    "Oranges": .7,
    "Plum": .6,
    "Bell": .4,
    "Melon": .2,
    "Bar": .1
  }

  for i in results:
    total += money_dict[1]
  print("total)", total)
  return total_earned += total

main()