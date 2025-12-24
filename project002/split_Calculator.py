print("Welcome to the split Calculator")
total_bill = float(input("Enter your Total Bill: "))
tip = float(input("How much tip would you like to give? 5%, 10% or 15%? "))
Num_members = int(input("How many members would you like to split? "))
result = tip / 100 * total_bill + total_bill
print("Each person should pay $", result)