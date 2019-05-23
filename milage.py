# print("How many kilometers did you cycle today")
# kms=input()
# miles=float(kms)/1.60934
# miles=round(miles,2)
# print("Ok,you said {k} miles {m}".format(k=kms,m=miles));


#data= input("What is your favorite color?")
#print ("You said {}".format(data))

# print("What's your favorite color?")
# data = input()
# print("You said" + data)

age = int(input("How old are you:"))

#if age != "":
if age:
    if age >=18 and age <=21:
        print("you can enter,but need a wristband!")
    elif age >=21:
        print("you can drink")
    else:
        print("you can't drink")
else:
    print("Please enter an age")