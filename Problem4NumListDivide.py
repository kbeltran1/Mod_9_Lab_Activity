counter = 0
tens = []

while counter < 50:
    if counter % 10 == 0:
        tens.append(counter)
    counter += 1

print(tens)

# Kelly Beltran
# 03-10-24
# Problem 4: Any empty list is created and counter is used to get to 50
# within counter numbers divisible by ten are appended  into tens list and list is printed