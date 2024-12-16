 #program that calculatesthe sum of all elements in a list of numbers.

list = [10, 9, 7, 5]
print(list)

# sum of elements
sum=0
for i in range(len(list)):
 sum = sum+list[i]
print("sum of list: ",sum)