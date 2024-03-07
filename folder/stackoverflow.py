#Ask for number input
first = int(input('Please type a number: '))
second = int(input('Please type a number: '))
third = int(input('Please type a number: '))
fourth = int(input('Please type a number: '))
fifth = int(input('Please type a number: '))
sixth = int(input('Please type a number: '))
seventh = int(input('Please type a number: '))
eighth = int(input('Please type a number: '))
ninth = int(input('Please type a number: '))
tenth = int(input('Please type a number: '))

#create a list for variables
sorted_list = [first, second, third, fourth, fifth, sixth, seventh, eighth, ninth, tenth]
dd_numbers = []

    #filter list and add odd numbers to new list
for value in sorted_list:
    if value%2 != 0:
    odd_numbers.append(value) 
        print ('The greatest odd number you typed was:'), max(odd_numbers)