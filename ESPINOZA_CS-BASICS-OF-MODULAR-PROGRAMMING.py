distance = 42.195
def time(speed):
    minutes = (distance / speed) * 60
    hours = int(minutes // 60)
    total_minutes = int(minutes % 60)
    return (f"At {speed} km/h, it will take approximately "
            f"{hours} hours and {total_minutes} minutes to finish a marathon.")
if __name__ == "__main__":
    try:
        speed_input = float(input("Enter the runner's average speed in km/h: "))
        if speed_input <= 0:
            print("Please enter a speed greater than zero.")
        else:
            finish_time = time(speed_input)
            print(finish_time)
    except ValueError:
        print("Invalid input. Please enter a number for the speed.")
    
#What is the purpose of the function you created?

    #The purpose of the function "time", is that in that function it will specifically solve the time which is the hours and minutes and it doesn't include anything unnessecary that's not related to time. Because of this, the code will not be messy, it will be much simpler to understand and the function can be reusable anytime.
    
#Identify which variables are global and which are local in your code.

   #distance - global
   #speed - local
   #total_minutes - local
   #hours - local
   #minutes - local
   #speed_input - local
   #finish_time - local
   
#Why is variable scope important?

   #Variable scope is important in order for us to organize our code effectively. Like for example, if we want to use a variable with the same value in different functions then we declare the variable outside of the functions for it to be global. The local variables are built inside the function to serve a specific purpose within that function. It also prevents interfering with other lines of code.
