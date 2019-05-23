## FOR LOOP LIST

# colors =["purple","teal","magenta",True,8.9]

# for color in colors:
#     print(color)

# number = [4,5,6,8,7,10]

# for num in number:
#     print(num*num)

## WHILE LOOP LIST

# colors =["purple","teal","magenta","crimson","emerald"]

# index = 0
# while index < len(colors):
#     print("{} : {}".format(index,colors[index]))
#     index += 1

#LIST METHODS APPEND INSERT AND EXTEND

#Append and Extend add end of the list
#Append
# data = [1,2,3]
# data.append(7)
# print(data)

#Extend
# num =[1,2,3]
# num.extend([4,5,6])
# print(num)

#insert add item at a given position
# num = [1,2,4,5,6]
# num.insert(2,"Hi")
# print(num)

#LIST OF METHODS: CLEAR,POP AND REMOVE
# #delete last item
# items = ['sock','mug','tea pot','cat food']
# items.pop()
# print(items)
# #delete (2) - 3rd item
# items = ['sock','mug','tea pot','cat food']
# items.pop(2)
# print(items)

#clear all list
# items = ['sock','mug','tea pot','cat food']
# items.clear()
# print(items)

#remove
# names =["colt","blue","arya","lena","colt","selena","pablo"]
# names.remove("arya")
# print(names)

#LIST METHODS:INDEX COUNT SORT REVERSE AND JOIN
#index
#names =["colt","blue","arya","lena","colt","selena","pablo"]
# print(names.index("colt"))
# print(names.index("colt",1))

#counts
# print(names.count("colt"))
# print(names.count("arya"))

#reverse
#names.reverse()
#print(names)

#sort
# names.sort()
# print(names)

#joins
#print("I am friends with:" .join(names))
# friends = ",".join(names)
# print(friends)

#Slices
# colors =["red","orange","green","yellow","blue","indigo"]
# print(colors[2:])
# print(colors[0:])
# print(colors[-2:])
# print(colors[2:4])
# print(colors[0:5:2])
# print(colors[2::-1])
# print(colors[:2:-1])

#NESTED LIST
coords=[[10.432,9.234],[32.456,6.544],[5.67,4.34]]

for loc in coords:
    for co in loc:
        print(co)
