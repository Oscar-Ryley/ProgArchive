#The code to import the data from Airports.txt. This places each line into different indexes of a list and then creates a different list for each overseas airport, finally putting each of these overseas airports' lists into a final list (thereby creating a two dimensional array).
airports = []
f = open("Airports.txt", "r")
lines = f.readlines()
for line in lines:
  line = line.replace("\n", "")
  airports.append(line)
#print(airports)

JFK = airports[0].split(",")
ORY = airports[1].split(",")
MAD = airports[2].split(",")
AMS = airports[3].split(",")
CAI = airports[4].split(",")

airports = [JFK, ORY, MAD, AMS, CAI]
#print(airports)

#The data from figure 2 in another 2 dimensional array.
type_table = [["Medium narrow body", 8, 2650, 180, 8], ["Large narrow body", 7, 5600, 220, 10], ["Medium wide body", 5, 4050, 406, 14]]

#These simple mathematical functions are needed in the functions later in the code. I created these functions after looking at the formulas needed on figure 3.
def no_standard(capacity_ifallstandard, no_firstclass):
  return(int(capacity_ifallstandard) - int(no_firstclass) * 2)

def flight_cost_per_seat(running_cost_perseat_per100km, distance_between_airports):
  return(float(running_cost_perseat_per100km) * int(distance_between_airports) /100)

def flight_cost(flight_cost_per_seat, nostandard, no_firstclass):
  return(float(flight_cost_per_seat) * (int(nostandard) + int(no_firstclass)))

def flight_income(no_firstclass, price_firstclass, no_standard, price_standard):
  return(int(no_firstclass) * float(price_firstclass) + int(no_standard) * float(price_standard))

def flight_profit(flight_income, flight_cost):
  return(flight_income - flight_cost)

#This simply error catches and takes the names of the UK airport involved in the flight and then does the same for the overseas airport- checking if the inputted airport code is present in Airports.txt.
def enter_airport():
  print("Please enter the three letter airport code for the UK Airport (LPL or BOH)")
  while True:
    choice = str(input())
    choice = choice.upper()
    if choice == "LPL":
      ukairport = "LPL"
      break
    elif choice == "BOH":
      ukairport = "BOH"
      break
    else:
      print("[Input incorrect, Please enter either BOH (Bournmouth international) or LPL (Liverpool John Lennon)]")
  print("Now enter the three letter airport code for the Overseas Airport")
  t = 0
  while t == 0:
    choice = str(input())
    choice = choice.upper()
    for i in airports:
      if i[0] == choice:
        overseasairport = choice
        print("The name of that Airport is", i[1])
        t = 1
    if t == 0:
      print("[That cannot be found in our list of overseas airports]")
  return(ukairport, overseasairport)

#This function first takes the type of aircraft used for the journey and then outputs the details for the aircraft in question. Then it takes a second error caught variable- the number of first-class seats. This function has to check if the number of first-class seats is valid when put against the aircraft type.
def enter_flight():
  print("""
Please enter the type of aircraft that should be used
MNB for Medium Narrow Body
LNB for Large Narrow Body  
MWB for Medium Wide Body
""")
  while True:
    choice = str(input())
    choice = choice.lower()
    if choice == "mnb":
      aircraft_type = 0
      atype = "MNB"
      print("""
Type: Medium narrow body
Running cost per seat per 100 km: £8
Maximum flight range (km): 2650
Capacity if all seats are standard-class: 180
Minimum number of first-class seats (if there are any): 8
""")
      break
    elif choice == "lnb":
      aircraft_type = 1
      atype = "LNB"
      print("""
Type: Large narrow body
Running cost per seat per 100 km: £7
Maximum flight range (km): 5600
Capacity if all seats are standard-class: 220
Minimum number of first-class seats (if there are any): 10
""")
      break
    elif choice == "mwb":
      aircraft_type = 2
      atype = "MWB"
      print("""
Type: Medium wide body
Running cost per seat per 100 km: £5
Maximum flight range (km): 4050
Capacity if all seats are standard-class: 406
Minimum number of first-class seats (if there are any): 14
""")
      break
    else:
      print("[Input incorrect, Please enter one of the options (MNB, LNB, MWB)]")
  print("Please enter the number of first-class seats")
  while True:
    d = 1
    choice = input()
    if choice.isdigit() == False:
      print("[Please enter a number]")
      d = 0
    if d == 1:
      no_first = int(choice)
      if no_first < type_table[aircraft_type][4]:
        print("[The number that you entered is less than the minimum number of first-class seats for this type of aircraft]")
      elif no_first > (int(type_table[aircraft_type][3]) /2):
        print("[The number of first-class seats is more than half the capacity if all the seats are standard class]")
      else:
        no_standardclass = no_standard(int(type_table[aircraft_type][3]), no_first)
        return(atype, int(no_standardclass), int(no_first))

#This feature takes all of the inputted data and shows the user different data relating to the cost, income and profit of what the inputted flight would be like.
def enter_priceplan_calprofit(uk, overseas, aircraft_type, no_firstclass, no_standardclass):
  #This section only continues the function if all neccissary data has already been inputted by the user in the other two sections
  t = 1
  if uk == "none":
    print("[Please enter a UK airport in the Airport Details section]")
    t = 0
  if overseas == "none":
    print("[Please enter a UK airport in the Airport Details section]")
    t = 0
  if aircraft_type == "none":
    print("[Please enter an Aircraft type in the Flight Details section]")
    t = 0
  if no_firstclass == "none":
    print("[Please enter a number of first class seats in the Flight Details section]")
  if t == 1:
    print("Please enter the price for a first-class and a standard-class seat (in the layout 0.00):")

    #This 'while loop' error catches the inputting of the seat prices for the flight as two float values rounded to 2 decimal places (because they are money values).
    while True:
      x = 0
      fprice = input("First-Class seat price:  ")
      try:
        fprice = float(fprice)
        fprice = round(fprice, 2)
        x = 1
        break
      except:
        print("[Please enter a price for the First-Class seat (in a float format)]")
      if x == 1:
        break
    while True:
      x = 0
      sprice = input("Standard-Class seat price:  ")
      try:
        sprice = float(sprice)
        sprice = round(sprice, 2)
        x = 1
        break
      except:
        print("[Please enter a price for the Standard-Class seat (in a float format)]")
      if x == 1:
        break
    
    #This section calculates the set of profit data requested by the user. It first collects all of the needed data to calculate each variable. Then it uses the mathematical functions defined at the start of the program to calculate profit data.
    if aircraft_type == "MNB":
      atypecost = 8
    elif aircraft_type == "LNB":
      atypecost = 7
    elif aircraft_type == "MWB":
      atypecost = 5

    if overseas == "JFK":
      o = 0
    elif overseas == "ORY":
      o = 1
    elif overseas == "MAD":
      o = 2
    elif overseas == "AMS":
      o = 3
    elif overseas == "CAI":
      o = 4

    if uk == "LPL":
      airport_distance = airports[o][2]
    elif uk == "BOH":
      airport_distance = airports[o][3]

    costperseat = round(flight_cost_per_seat(atypecost, airport_distance), 2)
    cost = round(flight_cost(costperseat, no_standardclass, no_firstclass), 2)
    income = round(flight_income(no_firstclass, fprice, no_standardclass, sprice), 2)
    profit = round(flight_profit(income, cost), 2)
    print("""
  PROFIT DATA:
    Cost Per Seat: £{}
            Cost:  £{}
          Income:  £{}
          Profit:  £{}
    
    """ .format(costperseat, cost, income, profit))

#The Main menu that user interacts with. This encloses all other sections and their functions as well as all data that is used throughout the program. It encloses the entire program in a 'while loop' until the user specifically asks to quit the program.
def menu():
  #Sets all of the data variables to 'none' to avoid errors when no data has been entered at the start of the program.
  aircraft_type = "none"
  no_standardclass = "none"
  ukairport = "none"
  overseasairport = "none"
  no_firstclass = "none"
  while True:
    #The main menu UI, includes all currently inputted data for accessibility and asks for the main menu input that will be taken as a string to be checked against the different acceptable options.
    print("""
  MAIN MENU
_____________________________________
  CURRENT DATA:
  UK Airport- {}
  Overseas Airport- {}
  Aircraft Type- {}
  Number of Standard-Class Seats- {}
  Number of First-Class Seats- {}

  Please enter the code for one of the following options:

  a) Enter Airport Details
  b) Enter Flight Details
  c) Enter Price Plan and Calculate Profit
  d) Clear Data
  q) Quit.
    """ .format(ukairport, overseasairport, aircraft_type, no_standardclass, no_firstclass))
    choice = str(input())
    choice = choice.lower()
    #print(choice)
    if choice == "a" or choice == "enter airport details":
      ukairport, overseasairport = enter_airport()
      input("PRESS ENTER TO CONTINUE")
      #replit.clear()
    elif choice == "b" or choice == "enter flight details":
      aircraft_type, no_standardclass, no_firstclass = enter_flight()
      input("PRESS ENTER TO CONTINUE")
      #replit.clear()
    elif choice == "c" or choice == "enter price plan and calculate profit":
      enter_priceplan_calprofit(ukairport, overseasairport, aircraft_type, no_firstclass, no_standardclass)
      input("PRESS ENTER TO CONTINUE")
      #replit.clear()
    elif choice == "d" or choice == "clear" or choice == "clear data":
      #To clear all of the data each variable is set to the string 'none'. The fact that this means the variable is empty is reflected later on in the code.
      aircraft_type = "none"
      no_standardclass = "none"
      ukairport = "none"
      overseasairport = "none"
      no_firstclass = "none"
      input("ALl data has been cleared, PRESS ENTER TO CONTINUE")
      #replit.clear()
    elif choice == "q" or choice == "quit":
      print("The program is ending...")
      break
    else:
      print("[Please enter one of the letters shown below in the main menu]")

#A function used to enclose the entire program, this is only used to make sure my title text is only printed once and to enclose the real main function- menu().
def main():
  print("""
  FLIGHT PLANNING
      by Oscar Ryley (CANDIDATE NUMBER: 7730)
  """)
  menu()

#After all of the function-ception involved in the rest of the program, the only function that is called is the main() function that will immeadiately run the all-encompassing menu() function.
main()