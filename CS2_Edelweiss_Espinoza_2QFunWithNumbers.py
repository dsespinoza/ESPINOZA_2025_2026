print("\n" * 2) #This multiplication here adds some space before the ascii art.
print("  _    _ _____   _______ _    _ ______ _____  ______ _ ")
print(" | |  | |_   _| |__   __| |  | |  ____|  __ \|  ____| |")
print(" | |__| | | |      | |  | |__| | |__  | |__) | |__  | |")
print(" |  __  | | |      | |  |  __  |  __| |  _  /|  __| | |")
print(" | |  | |_| |_     | |  | |  | | |____| | \ \| |____|_|")
print(" |_|  |_|_____|    |_|  |_|  |_|______|_|  \_\______(_)")
print("\n" + "=" * 45)
print("     FUN WITH NUMBERS: SUM TO YOUR AGE")
print("=" * 45)
print("\n")

#These line of codes here initializes the variables.
total_sum = 0
counter = 1
age = 0

#--- Start of the inputing the age loop ---

#For here, I used a while loop to check the errors when inputting the age.
#The loop continues as long as a valid age hasn't been set.
while age <= 0:
    try:
        #This inputs the user's age.
        input_str = input("Please enter your age: ")
        age = int(input_str)
        
        #Here, it checks for negative numbers as well as zero.
        if age <= 0:
            print("❌ Invalid entry: Please enter a positive whole number.")
            
    except ValueError:
        #This code here catches errors if the user inputs a word.
        print("❌ Invalid entry: Please enter a whole number (no words or decimals).")

#--- End of the input loop ---

#--- Start of the calculation loop ---

#This part is where the calculation happens.
#I also used a while loop here. It functions to count and add the age.
#This loop continues as long as the counter is less than or equal to the age.
while counter <= age:
    #This adds the present value of the counter to the sum variable.
    total_sum += counter
    
    #This is crucial, because if the counter surpasses the age then it identifies as false then it stores the intended number.
    counter += 1

#--- End of the calculation loop ---

#And finally, this part displays the answer!
print("-" * 45)
print(f"🎉 Result: The sum of all numbers from 1 to {age} is: {total_sum}")
print("-" * 45)
