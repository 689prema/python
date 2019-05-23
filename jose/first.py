#print "Hello";
a=5;
#print a;
a=10;
a= a + a;
#print a;
a= a +a ;
#print a;
#print type(a);
a=30.1;
#print type(a);

my_income =100;
tax_rate=0.1;
my_taxes =my_income * tax_rate;
#print my_taxes;

#String
#print "hello world one";
#print " hello world two";
#print len('hello');

#indexing and slicing
#mystring = 'Hello World';
#mystring[0];
#print mystring[-1];

#mystring = 'abcdefghijk'
#print mystring[2:];
#print mystring[:3];
#print mystring[3:5];
#print mystring[6:9];
#print mystring[::2];
#print mystring[::-1];

#String Concatenation

#x= 'Hello World';
#x . "it is beautiful outside!";
#print x + "it is beautiful outside";
#x= x + " it is so beautiful outside";
#print x;
# x = x.upper();
# print x;
# x= x.lower();
# print x;
# x=x.split('i');
# print x;

#print formatting

# print "This is a string {}".format('INSERTED');
# print "The {} {} {}".format('fox','brown','quick');
# print "The {2} {1} {0}".format('fox','brown','quick');
# print "The {q} {f} {b}".format(f='fox',b='brown',q='quick');

# result = 800/777;
# print result;
# print "The result is {r:1.3f}".format(r=result);

# name="prema";
# print "Hello,her name is {}".format(name);

#LISTS
# mylist =['one','23.4','ram'];
# print mylist;
# another_list = ['four','five'];
# new_list = mylist + another_list;
# print new_list;
# new_list.append('six')
# print new_list
# new_list.pop()
# print new_list
# new_list.pop(0)
# print new_list

# new_list=['c','e','h','b','g','a'];
# new_list.sort();
# print new_list;
# num=[5,3,1,4,6,7,2];
# num.sort();
# print num;

#DICTIONARY
# my_dict={'key1':'value1','key2':'value2'};
# print my_dict['key1'];
d={'k1':123,'k2':[0,1,2],'k3':{'insidekey':100}}
print d['k2']
print d['k3']['insidekey']
print d.keys();
print d.values();
print d.items();