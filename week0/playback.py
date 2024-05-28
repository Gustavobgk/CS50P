"""talk = input("Say something!")
x,b,c = talk.split(" ")
print(f"{x}...{b}...{c}")
user = input("Say something!")
def talking(talk):
    print(talk.split("..."))
talking(user)
"""

txt = input("Say something! ")
x = txt.split(" ")
print(x)
joined_string = "...".join(x)
print(joined_string) 

#print(x, sep="...")