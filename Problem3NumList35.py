numbers = []
total = 0

while total <= 100:
    num = int(input("Enter a number: "))
    total += num
    numbers.append(num)

print("Total sum of numbers:", total)
print("List of numbers:", numbers)

# Kelly Beltran
# 03-10-24
# Problem 3: User is asked to input numbers and is continuously asked until sum of numbers is > 100
# List of numbers and sum of numbers is also printed when loop is complete