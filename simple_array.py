#List of array
numbers = [0, 1, 2, 3, 4, 5]

#print some numbers by the indexes
print(numbers[0])   #0
print(numbers[3])   #3
print(numbers[2])   #2
print(numbers[-1])  #5

print ("Index 1 is:", numbers[1])
numbers[1] = 25      #change index 1 to hold value 25
print (numbers[1])   #should print 25
print("Index 1 is:", numbers[1])

print(len(numbers))
numbers.remove(3)
print("Removing value 3.")
print(len(numbers))
print ("\n")

#what will this print
arr = [4,8,12,16]
print ("arr = [4,8,12,16] \n print(arr[1])")
print(arr[1])      #8

numbers.append(40)
print(numbers)
print ("\n")

#what will this print
print("print(len(numbers))")
print(len(numbers))    #6
print ("\n")

numbers = [5,10,15,20]
total = 0
for number in numbers:
  total += number

print (total)
print ("\n")

numbers = [12,3,5,28,9,17]
largest = numbers[0]
for number in numbers:
  if number > largest:
    largest = number
print ("numbers = [12,3,5,28,9,17]")
print ("largest number is:",largest)
smallest = numbers[0]
for number in numbers:
  if number < smallest:
    smallest = number
print ("smallest number is:", smallest)
print ("\n")

numbers = [2,7,10,13,16,21,24]
even = 0
for number in numbers:
  if number % 2 == 0:
    even += 1
print(even)

numbers = [1,2,3,4,5]
print ("numbers = [1,2,3,4,5]")
reversed_numbers =[]
hold = 5    # index 5
while hold > 0:
  reversed_numbers.append(numbers[hold-1])
  hold -= 1
print("reversed_number", reversed_numbers, "\n")

#it is taking the index [hold-1] of array (numbers) to append to array (reversed_numbers)

#Remove 0 from the list
numbers = [0, 5, 0, 3, 8, 0, 2]
print ("numbers = [0, 5, 0, 3, 8, 0, 2] Remove 0")
result = []
for number in numbers:
  if number > 0:
    result.append (number)
print("result",result,"\n")

#Count how many times a number appears
numbers = [2, 5, 2, 8, 2, 3, 5]
print ("numbers = [2, 5, 2, 8, 2, 3, 5]. Count how many times a number appears")
target = 2
count = 0
for number in numbers:
    if number == target:
      count += 1
print("The number", target, "appears", count, "times. \n")

#Find duplicate numbers
numbers = [4, 7, 4, 2, 7, 9, 3]
print("numbers = [4, 7, 4, 2, 7, 9, 3] Find duplicate numbers")
duplicates = []

for number in numbers:
  if numbers.count(number) > 1 and number not in duplicates:
    duplicates.append(number)
print(duplicates, "\n")

#Find evens and odds
numbers = [12, 7, 5, 8, 3, 10, 15, 4]
print ("numbers = [12, 7, 5, 8, 3, 10, 15, 4]. Find evens and odds")
even_numbers = []
odd_numbers = []

for number in numbers:
    if number % 2 == 0:
      even_numbers.append(number)
    else:
      odd_numbers.append(number)

print("Even:", even_numbers)
print("Odd:", odd_numbers, "\n")

#Remove duplicates while keeping the original order
numbers = [3, 5, 3, 8, 5, 2, 8, 9]
print ("numbers = [3, 5, 3, 8, 5, 2, 8, 9].\nRemove duplicates while keeping the original order")
unique_numbers = []

for number in numbers:
  if number not in unique_numbers:
    unique_numbers.append(number)
print(unique_numbers, "\n")

#Find the second largest number
numbers = [12, 5, 28, 9, 17, 28]
print ("numbers = [12, 5, 28, 9, 17, 28]. Find the second largest number")
largest = float('-inf')
second_largest = float('-inf')

for number in numbers:
    if number > largest:
      second_largest = largest
      largest = number
    elif number < largest and number > second_largest:
      second_largest = number
print("Second largest:", second_largest, "\n")

#Find the most frequent number
numbers = [4, 7, 4, 2, 7, 4, 9, 7, 7]
print("numbers = [4, 7, 4, 2, 7, 4, 9, 7, 7]. Find the most frequent number")
most_frequent = numbers[0]
highest_count = 0

for number in numbers:
    if numbers.count(number) > highest_count:
      most_frequent = number
      highest_count = numbers.count(number)
      
print("Most frequent number:", most_frequent)
print("Occurrences:", highest_count, "\n")

#Move all the zeros to the end
numbers = [0, 5, 0, 3, 8, 0, 2]
print ("numbers = [0, 5, 0, 3, 8, 0, 2]. Move all the zeros to the end")
result =[]
count = 0
for number in numbers:
  if number != 0:
    result.append(number)
for number in numbers:
  if number == 0:
    count += 1
for i in range(count):
  result.append(0)
print(result)

#Find third largest
numbers = [12, 5, 28, 9, 17, 28, 21, 17]
print ("numbers = [12, 5, 28, 9, 17, 28, 21, 17]. Find the third largest")
largest = float('-inf')
second_largest = float('-inf')
third_largest = float('-inf')

for number in numbers:
    if number == largest or number == second_largest:
      continue
    if number > largest:
      third_largest = second_largest
      second_largest = largest
      largest = number
    elif number > second_largest:
      third_largest = second_largest
      second_largest = number
    elif number > third_largest:
      third_largest = number
print("Third largest:", third_largest, "\n")
