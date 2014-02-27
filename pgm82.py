# Jesse Hammond

# If this truly is the formula, I wonder how oft that formula has been revised over the years...
# In any case, this is a program to compute wind chill index from a given temperature and wind speed, or to print a wind chill chart.

# Formula: 35.74 + 0.6215T – 35.75(V0.16) + 0.4275T(V0.16), where T=Temperature and V=Wind Speed

# Pseudocode:
# Ask whether the user wishes to get a graph or input the values manually. Loop until valid input is given.
# If a graph:
#    Print out the column headers (-20 to 60, by 10's).
#    For each wind chill 0-50, by 5's, output a divider between rows, then the wind speed, then...
#       For each Temperature/Wind Chill combo, print a divider between columns and the proper value (given by formula above).
# If values:
#    Get the values for temperature and wind chill
#    Calculate the value from the formula above and print it out.

def main():
    choice = input("This program calculates wind chill from temperature (Fahrenheit) and wind speed.\nPlease choose one of the following:\na: Input temperature and wind speed manually\nb: Generate table\nOther: Exit\n> ") # Gets user's choice on what to generate, if anything.
    if choice=="a": # If they choose manual input...
        temperature = input("\nInput temperature (omit ° and F):\n> ") # These two lines get temperature and wind speed.
        wind = input("\nInput wind speed:\n> ")
        try:
            print("\nThe wind chill is {0}°F.".format(round(35.74+(0.6215*float(temperature))-(35.75*(float(wind)**0.16))+(0.4275*float(temperature)*(float(wind)**0.16))))) # If the formula is successful, print the result.
        except ValueError: # If not, print an error and exit.
            print("\nInvalid input.")
            return
    elif choice=="b": # If they choose a table...
        print("     |-20°|-10°|  0°| 10°| 20°| 30°| 40°| 50°| 60°") # Print the top labels of the table.
        for wind in [0,5,10,15,20,25,30,35,40,45,50]: # For each column...
            tempStr = "-----+----+----+----+----+----+----+----+----+----\n{0:>2}MPH".format(wind) #Pring the left labels of the table, as well as the dividing line between rows.
            for temperature in [-20,-10,0,10,20,30,40,50,60]: # For each row...
                tempStr+= "|{0:>3}°".format(round(35.74+(0.6215*float(temperature))-(35.75*(float(wind)**0.16))+(0.4275*float(temperature)*(float(wind)**0.16)))) # Print the temperature in that cell.
            print(tempStr)
main()

# On another note, good HEAVENS, the 0MPH row is strange. I thought it was in error, until I calculated the first cell and realized, indeed, it was right, according to the formula.