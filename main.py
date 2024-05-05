counter = 0 
print("Number Guessing Game")
print()
print("Enter a nuber between 1 and 1,000,000")
print()
userinput = 0
answer = 60
while (userinput != answer) :
 userinput = input("What is your guess? ")
 counter = counter +1

 if int(userinput) == answer :
   print("correct !!")
   print("It took you", counter, "guesses to get it correct!") 
   break
 elif int(userinput) < answer :
   print("too low")
 elif int(userinput) > answer :
   print("too high")
 if int(userinput) <  0 :
   print("You have entered a negitive number")
   break
      

