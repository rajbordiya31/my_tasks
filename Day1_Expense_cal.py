print("Expense Calculator")


food = 0
travel = 0
rent= 0
other = 0

while True:
    # Write Category
    category = input("Enter your category(Food / Travel / Rent / Other) : ")
    if category.lower()== "done":
        break
    # Write Amount
    amount = float(input("Enter your expense amount : "))
    
    if category.lower() == "food":
        food = food+amount

    elif category.lower() == "travel":
        travel = travel+amount

    elif category.lower() == "rent":
        rent = rent+amount

    else:
        other=other+amount
    
    print("Food = rs",food)
    print("Travel = rs",travel)
    print("Rent = rs",rent)
    print("Other = rs",other)
    
total_expense =food+travel+rent+other
print("total expense ",total_expense)
    
    
    


    

