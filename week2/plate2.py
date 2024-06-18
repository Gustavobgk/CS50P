def main():
    plate = input("Plate: ")
    print(len(plate))
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def minimum(s):
    if len(s) <= 6 and len(s) >= 2:
        return True 

def middle_checker(plate):
    for i in range(1, len(plate) - 1):
        if plate[i].isnumeric() and (plate[i-1].isalpha() or plate[i-2].isalpha() or plate[i-3].isalpha() ) and plate[i+1].isalpha():
            return False
    return True

def zero_checker(s):
    index = 0
    for char in s:        
        if char.isdigit():
            index += 1  # Corrected assignment
            if index == 1 and char == "0":
                return False
                
    return True

def filters(s):
    for things in s:        
        if things == "," or things == "." or things == " ":
            return False
    return True
    

"""    check_list = []
    for num in s:
        if num.isdigit():
            check_list.append(num)"""
                
def is_valid(s):
    if len(s)<2:
        return False
    return s[0].isalpha() and s[1].isalpha() and minimum(s) and middle_checker(s) and zero_checker(s) and filters(s)



main()