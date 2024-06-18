def main():
    text = input("Input:")
    print(convert(text))

def convert(txt):
    text = []
    for t in txt:
        if t.lower() == "a" or t == "e" or t == "i" or t == "o" or t == "u":
            pass
        else:
            text.append(t) 
    new_string = ''.join(text)
    return new_string

main()