import numpy as np
#Tracking spending (in Pesos) over four weeks.
#Rows: Categories (Groceries, Transport, Bills, Entertainment)
#Columns: Weeks (Week 1, Week 2, Week 3, Week 4)

#Reflection:
#Why did you choose this dataset?
#I chose the monthly budget tracker because managing personal finances is one of the essential parts of everyday life. This dataset is excellent for tracking spending habits, providing insights for budgeting, and also identifying areas for savings. It provides clear data in how money is allocated in each category in a certain week, thus making it an efficient dataset.

#How does a 2D array help organize and work with this kind of data?
#The 2D array is helpful because it separates the two dimensions of data with the 'what' (rows) and the 'when' (columns). This allows the user to calculate the total monthly spend for a single category (a row sum) or determining the average weekly cost of transport efficiently, which is useful for data analysis. The user can also change the data in a specific week or category, making it effective for fast data analysis. The dual-axis organization makes the data well-organized.

spending = np.array([
    [2500, 3000, 2000, 2800], #Groceries
    [800, 750, 900, 850], #Transport
    [1500, 1500, 1500, 1500], #Bills
    [500, 1200, 300, 600]  #Entertainment
])


categories = ["Groceries", "Transport", "Bills", "Entertainment"]
weeks = ["Week 1", "Week 2", "Week 3", "Week 4"]

#Side Functions

def print_data(data, categories):
    #Prints the current state of the 2D array data.
    print("\n--- Current Spending Data ---")
    
    #Prints headers
    print("{:<15}".format("Category"), end="")
    for w in weeks:
        print("{:>8}".format(w), end="")
    print("\n" + "-"*47)

    #Prints the data
    for i in range(len(data)):
        print("{:<15}".format(categories[i]), end="")
        for amount in data[i]:
            print("{:>8}".format(amount), end="")
        print()
    print("-----------------------------")


def select_data(data, categories):
    #Allows user to view data for a single category.
    print("\n[2] Select category")
    for i, cat in enumerate(categories):
        print(f"[{i}] {cat}")
    
    try:
        choice = int(input("Enter choice: "))
        if 0 <= choice < len(categories):
            print(f"\n{categories[choice]}")
            print(data[choice])
        else:
            print("Invalid category selection.")
    except ValueError:
        print("Invalid input. Please enter a number.")


def update_data(data, categories, weeks):
    #Allows user to update a specific value.
    print("\n[3] Update data")
    
    #Select Category (Row)
    for i, cat in enumerate(categories):
        print(f"[{i}] {cat}")
    
    try:
        cat_choice = int(input("Enter choice: "))
        if not (0 <= cat_choice < len(categories)):
            print("Invalid category selection.")
            return
            
        #Select Week (Column)
        print(f"--- Updating {categories[cat_choice]} ---")
        for j, week in enumerate(weeks):
            print(f"[{j}] {week}")
            
        w_choice = int(input("Enter choice: "))
        if not (0 <= w_choice < len(weeks)):
            print("Invalid week selection.")
            return

        #Enter New Value
        new_data = int(input("Enter new spending amount (Pesos): "))
        
        #Perform Update
        data[cat_choice][w_choice] = new_data
        
        #Confirmation Output
        print(f"\nUpdating spending for {categories[cat_choice]} on {w_choice} to {new_data} Pesos")
        print(f"Updated data: {categories[cat_choice]}")
        print(data[cat_choice]) 

    except ValueError:
        print("Invalid input. Please enter a number.")


def summarize_data(data, categories):
    #Calculates sum, mean, min, and max for each category
    print("\n[4] Summarize data")
    print("------------------------------------------------------------------")
    print("{:<15} {:>8} {:>10} {:>5} {:>5}".format(
        "Category", "Total (₱)", "Avg/Week", "Min", "Max"
    ))
    print("------------------------------------------------------------------")
    
    for i in range(len(data)):
        row = data[i]
        
        
        total = sum(row)
        avg = np.mean(row)
        min_val = min(row)
        max_val = max(row)

        #Prints the results
        print("{:<15} {:>8} {:>10.2f} {:>5} {:>5}".format(
            categories[i],
            total,
            avg,
            min_val,
            max_val
        ))
    print("------------------------------------------------------------------")


#Main Functions

def run_menu():
    while True:
        #Main Menu
        print("\n[1] Print all data")
        print("[2] Select category")
        print("[3] Update data")
        print("[4] Summarize data")
        print("[5] Exit")
        
        choice = input("Enter choice: ")
        
        if choice == '1':
            print_data(spending, categories)
        elif choice == '2':
            select_data(spending, categories)
        elif choice == '3':
            update_data(spending, categories, weeks)
        elif choice == '4':
            summarize_data(spending, categories)
        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


run_menu()