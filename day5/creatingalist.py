#python program to Creating a list
my_list = [10, 20, 30, 40, 50, 60]

# 1.Indexing - Accessing elements at a specific index
print("Indexing:")
print("Element at index 0:", my_list[0])
print("Element at index 2:", my_list[2])  
print("Element at index -1:", my_list[-1]) 
print("Element at index -2:", my_list[-2]) 

# 2.Slicing-Extracting a subset of the list
print("\nSlicing:")
print("Elements from index 1 to 4:", my_list[1:4]) 
print("Elements from index 2 to the end:", my_list[2:]) 
print("Elements from the beginning to index 3:", my_list[:3])
print("Every second element:", my_list[::2])  

# 3.Modifying a list
print("\nModifying a list:")
my_list[1] = 25 
print("After changing index 1 to 25:", my_list)
