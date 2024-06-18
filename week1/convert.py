def main():
   hours=input("")
   hours=convert(hours)

def convert(time):
   time = time.replace(":", " ")
   time = time.split()
   time[0] = int(time[0])
   print(time[2])
#    if time[2] == "a.m.":
#       if time[0] == 7 or time[0] == 8:
#          print("breakfast time")
#       elif time[0] == 12 or time[0] == 13:
#          print("lunch time")
   if time[0] == 7 or time[0] == 8:
      print("breakfast time")
   elif time[0] == 12 or time[0] == 13:
      print("lunch time")
   elif time[0] == 18 or time[0] == 19:
      print("dinner time")

if __name__ == "__main__":
    main()