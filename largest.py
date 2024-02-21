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

#Ask for number input
first = int(raw_input('Please type a number: '))
second = int(raw_input('Please type a number: '))
third = int(raw_input('Please type a number: '))
fourth = int(raw_input('Please type a number: '))
fifth = int(raw_input('Please type a number: '))
sixth = int(raw_input('Please type a number: '))
seventh = int(raw_input('Please type a number: '))
eighth = int(raw_input('Please type a number: '))
ninth = int(raw_input('Please type a number: '))
tenth = int(raw_input('Please type a number: '))

#create a list for variables
sorted_list = [first, second, third, fourth, fifth, sixth, seventh, 
              eighth, ninth, tenth]
odd_numbers = []

    #filter list and add odd numbers to new list
for value in sorted_list:
        odd_numbers.append(value)if value%2 != 0:
 print ('The greatest odd number you typed was:'), max(odd_numbers)