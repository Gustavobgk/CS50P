def main():
    camel_case = input("camelCase: ")
    snake_case = transform(camel_case)
    print(snake_case)

def transform(case):
    list_of_items = []
    for c in case:
        if c.isupper():
            list_of_items.append("_")
            list_of_items.append(c.lower())
        else:
            list_of_items.append(c)
    new_string = ''.join(list_of_items)
    return new_string

main()





























# def main():
#     camel_case=input("camelCase:")
#     transform(camel_case)

























# def transform(case):
#     for c in case:
#         if c.isupper() == True:
#             upper = c
#             index = case.index(upper)
#             new_string = case[:index] + "_" + case[index:]
#             print(new_string)
            
#     new_string = case[:index] + "_" + case[index:]
#     new_string = new_string.lower()    
#     print(new_string)
#     print(upper)

    # index = case.index(upper)
    # index = index - 1
    # case = case.split(upper)
    # case.insert(index,"_")
    # print(index)
    # print(case)

main()