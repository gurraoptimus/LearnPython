# a = [1,2,3,4,6,7,99,88,999]
#  for i in a:
#  max_num = 0
    #  if i > max_num:
        #  max_num = i
#  print(a.index(max_num))

# a = (1, 2, 3, 9)
# print(max(a))

# x = max("Oscar","Ozzle","MagicOA")
# print(x)

#tl = ["oscar","gurra","stoffe"]
#for name in tl:
#   print(name)

#for p in range(0,102,2):
    #print("Number"+ str(p))

# rs = 0
# for g in range(1001):
 # if g %2==1:
#       rs += g
#print(rs)

# import random
# res=[0,0,0,0,0,0,0,0,0,0]
#list=[5]
#for f in list:
#        res[f]+=1
#print(res)
#for x in range(1000):
   # list.append(random.randint(0,10))


#import random
#list=[]
#for x in range(1000):
#    list.append(random.randint(0,10))
#print(list)

# python Classes
class Person:
    def __init__(self, name):
        self.name = name
            
    def say_hello(self):
        print("hello {}!".format(self.name))

gurraoptimus = Person('GurraOptimus')
gurraoptimus.say_hello()