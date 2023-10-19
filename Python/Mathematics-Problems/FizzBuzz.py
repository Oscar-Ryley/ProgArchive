#2020 -GCSE

import os
os.system('cls')

print("""
Oscar Ryley's
            
             FizzBuzz
             Machine
""")

ubound = "a"
while ubound.isdigit() == False: 
  ubound = input("Number you want to FizzBuzz to: ")

os.system('cls')

for i in range(1, int(ubound) + 1):
  printable= ""
  
  if i % 3 == 0:
    printable += "Fizz"
  if i % 5 == 0:
    printable += "Buzz"
  
  if printable == "":
   print(i)

  else:
    print(printable)