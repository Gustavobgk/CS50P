cap=[50]
while cap[0] > 0:
    amount = int(input("Insert coin:"))
    if amount == 25 or amount == 10 or amount == 5:
           total = cap[0] - amount
           cap[0]= total 

    
    
    
    
    if cap[0] == 0:
        print(f"Change owed: {cap[0]}")
        break
    elif cap[0] < 0:
        print(f"Change owed: {abs(cap[0])}")
        break
    print(f"Amount due:{cap[0]}")