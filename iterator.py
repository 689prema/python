#ITERATOR

# nums = [1,2,3,4,5]
# it = iter(nums)
# it

# def my_for(iterable):
#     iterator = iter(iterable)
#     while True:
#       try:
#           print(next(iterator))
#       except StopIteration:
#           print("END OF ITERTOR")
#           break
#     #print(next(iterator))
    
# my_for("hello")

# class Counter:
#     def __init__(self,low,high):
#         self.current = low
#         self.high = high
    
#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.current < self.high:
#             num = self.current
#             self.current += 1
#             return num
#         raise StopIteration
        
# for x in Counter(50,70):
#     print(x)

#GENERATOR

def fib_gen(max):
    x=0
    y=1
    count = 0
    while count < max:
        x, y = y, x+y
        yield x
        count+=1
    
for n in fib_gen(10):
        print(n)
        