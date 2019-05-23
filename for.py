# for x in range(1,10):
#     print(x)
#     print(x*x)

# for letter in "coffee":
#     print(letter*10)
    
#EXCERCISE 1

# times=input("How many times do I have to tell you?")
# times=int(times)


# for time in range(times):
#     print("CLEAN UP YOUR ROOM! times {}".format(time+1))
#     #print(f"time{time+1}:CLEAN UP YOUR ROOM")
    
#EXCERCISE 2


for n in range(1,21):
    if n==4 or n==13:
        x="UNLUCKY!"
    elif n%2 == 0:
        x="even"
    else:
        x="odd"
    print("{} is {}".format(n,x) )