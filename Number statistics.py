number = int(input("Enter a number: "))
maximum = number
minimum = number
total = 0
count = 0
even_count = 0
odd_count = 0
positive_count = 0
negative_count = 0

while number != 0:
    total += number
    count += 1
    if number > 0:
        positive_count += 1
    elif number < 0:
        negative_count += 1
    if number > maximum:
        maximum = number
    if number < minimum:
        minimum = number
    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
    number = int(input("Enter a number: "))
if count > 0:
    average = total / count
    print(f"Total: {total}")
    print(f"Count: {count}")
    print(f"The average is: {average}")
    print(f"The even count is: {even_count}")
    print(f"The odd count is: {odd_count}")
    print(f"Maximum is: {maximum}")
    print(f"Minimum is: {minimum}")
    print((f"The positive count is: {positive_count}"))
    print((f"The negative count is: {negative_count}"))
else:
    print("No numbers entered")