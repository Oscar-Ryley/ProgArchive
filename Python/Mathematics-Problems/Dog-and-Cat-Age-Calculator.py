#2019 -GCSE

import os

os.system('cls')

print("""
The Dog and Cat age calculator

 ..^____/     ___________________________________/|
`-. ___ )    ( How old is our pet in human units? )
  ||  ||

                    for all of your frivolous needs


""")

while True:
  print("Is your pet a Cat or a Dog?")
  pettype = input()
  if pettype == "cat" or pettype == "dog":
    break
  else:
    print("***Enter a pet type***")

if pettype == "dog":
  while True:
    print("How big is your pet? (small, medium or large)")
    size = input()
    if size == "small" or size == "medium" or size == "large":
      break
    else:
      print("***Enter small, medium or large***")

while True:
  print("how old is your animal in human years?")
  humanyearsstr = input()

  if humanyearsstr.isdigit() == True:
    humanyears = int(humanyearsstr)
    break
  else:
    print("***Enter a number***")

os.system('cls')
actualyears = 0

if pettype == "dog":
  if humanyears <= 1:
    actualyears = 15
  elif humanyears >= 2:
    actualyears = 24 + (humanyears - 2) * 4

  if size == "medium":
    if humanyears > 7 and humanyears % 2 == 0:
      add = humanyears - 3
    else:
      add = humanyears - 4
    if add >= 1:
      actualyears += add

  if size == "large":
    if humanyears >= 6:
      actualyears += humanyears - 1
    if humanyears >= 16:
      actualyears += 15

if pettype == "cat":
  if humanyears <= 1:
    actualyears = 14
  elif humanyears >= 2:
    actualyears = 24 + (humanyears - 2) * 5

print("Your pet {}, is actually {} in {} years!".format(
    pettype, actualyears, pettype))
