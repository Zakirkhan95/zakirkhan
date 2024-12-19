#Code to study sets and various operations regarding that

#Creating sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("Set 1:", set1)
print("Set 2:", set2)

# 1.Union - All unique elements from both sets
union_set = set1.union(set2)
print("\nUnion of Set 1 and Set 2:", union_set)

# 2.Intersection - Common elements between both sets
intersection_set = set1.intersection(set2)
print("Intersection of Set 1 and Set 2:", intersection_set)

# 3.Difference - Elements in Set 1 but not in Set 2
difference_set = set1.difference(set2)
print("Difference (Set 1 - Set 2):", difference_set)

# 4.Symmetric Difference - Elements in either Set 1 or Set 2 but not both
symmetric_difference_set = set1.symmetric_difference(set2)
print("Symmetric Difference between Set 1 and Set 2:", symmetric_difference_set)

# 5.Subset - Check if Set 1 is a subset of Set 2
is_subset = set1.issubset(set2)
print("\nIs Set 1 a subset of Set 2?", is_subset)

# 6.Superset - Check if Set 1 is a superset of Set 2
is_superset = set1.issuperset(set2)
print("Is Set 1 a superset of Set 2?", is_superset)

# 7.Disjoint - Check if Set 1 and Set 2 have no elements in common
is_disjoint = set1.isdisjoint(set2)
print("Are Set 1 and Set 2 disjoint?", is_disjoint)