#CLEAR 
#d = dict(a=1,b=2,c=3)
# d.clear()
# print(d)

#COPY
# d= dict(a=1,b=2,c=3)
# c=d.copy()
# print(c)

#FROM KEYS
# new_user = {}.fromkeys(['name','score','email','profile bio'],'unknown')
# print(new_user)
# new_user.fromkeys(['phone'],'unknown')
# print(new_user)

#GET
# d= dict(a=1,b=2,c=3)
# print(d.get('a'))

#POP
#d= dict(a=1,b=2,c=3,d=4,e='eggs')
#d.pop('a')
#print(d)

#POP ITEM remove random
#d= dict(a=1,b=2,c=3,d=4,e='eggs')
#d.popitem()
#print(d)

#UPDATE
# instructor ={'name':'colt','num_courses':4,'favorite_language':'Python'}
# person = {"city":"Antigua"}
# person.update(instructor)
# print(person)
# print(instructor)

#DICTIONARY exercise1
# playlist ={
#     'title':'patagonia bus',
#     'author':'colt steele',
#     'songs':[
#         {'title':'song1','artist':['blue'],'duration':2.5},
#         {'title':'song2','artist':['kitty','djcat'],'duration':5.25},
#         {'title':'meowmeow','artist':['garfield'],'duration':2.0}
#         ]
# }
# total_length=0
# for song in playlist['songs']:
#     total_length += song['duration']
# print(total_length)

#DICTIONARY COMPREHENSION  Exercise1

# instructor ={'name':'colt','city':'san francisco','color':'purple'}
# yelling_instructor={k.upper():v.upper() for k,v in instructor.items()}
# print(yelling_instructor)

#Exercise2

# num_list =[1,2,3,4]
# n={num : ("even" if num % 2 == 0 else "odd") for num in range(1,100)}
# print(n)

instructor ={'name':'colt','city':'san francisco','color':'purple'}
yelling_instructor={(k.upper() if k is 'color' else k) :v.upper() for k,v in instructor.items()}
print(yelling_instructor)

