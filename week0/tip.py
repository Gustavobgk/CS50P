def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    d = d.replace("$","")
    d = float(d)
    d = d/100
    return d
    
    print(d)


def percent_to_float(p):
    p = p.replace("%", "")
    p = float(p)
    return p
    print(p)


main()