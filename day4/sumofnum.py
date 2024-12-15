#python prohram input a number to calculate the sum of its digits
number = int(input("Enter a number to calculate the sum of its digits: "))
original_number = number
sum_of_digits = 0

while number > 0:
    digit = number % 10
    sum_of_digits += digit
    number //= 10

print(f"The sum of the digits of {original_number} is: {sum_of_digits}")