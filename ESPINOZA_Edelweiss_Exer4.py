def f_to_c(f):
    return (f - 32) * 5/9

def k_to_c(k):
    return k - 273.15

def temp_status(c):
    if c < 0:
        return "Too cold"
    elif 0 <= c <= 35:
        return "Safe temperature"
    else:
        return "Too hot"

print("Welcome to the Temperature Status Program!")
print("Please choose a unit of measurement: Celsius (C), Fahrenheit (F), or Kelvin (K)")

unit = input("Enter your choice: ").upper()

if unit not in ['C', 'F', 'K']:
    print("Invalid unit of measurement. The program will now exit.")
else:
    try:
        temp_input = float(input(f"Enter the temperature in {unit}: "))

        if unit == 'F':
            c_temp = f_to_c(temp_input)
        elif unit == 'K':
            c_temp = k_to_c(temp_input)
        else:
            c_temp = temp_input

        status = temp_status(c_temp)
        print(f"The temperature status is: {status}")

    except ValueError:
        print("Invalid temperature value. The program will now exit.")
input("Press Enter to exit...")