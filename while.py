# Initialize variables
total = 0
count = 0

while True:
    number = int(input("Enter a number (enter -1 to stop): "))
    
    if number == -1:
        break  
    elif number == 0:
        print("0 is not a valid input. Please enter a different number.")
        continue 
    
    total += number
    count += 1

if count > 0:
    average = total / count
    print("The average of the valid numbers entered is:", average)
else:
    print("No valid numbers were entered.")


