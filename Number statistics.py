my_list = []
number = int(input("Enter a number: "))

count = 0
total = 0
average = 0
maximum = number
minimum = number
positive_count = 0
negative_count = 0
even_count = 0
odd_count = 0



while number != 0:
    if number > 0:
        positive_count += 1
    else:
        negative_count += 1
    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1


    my_list.append(number)
    count += 1
    total = total + number
    average = total / count
    maximum = max(my_list)
    minimum = min(my_list)
    result = sorted(my_list)
    result2 = sorted(my_list, reverse=True)
    number = int(input("Enter another number: "))
if count == 0:
    print("No numbers entered")
else:
    print(f"Original : {my_list}")
    print(f"Count: {count}")
    print(f"Total: {total}")
    print(f"Average: {average}")
    print(f"Maximum: {maximum}")
    print(f"Minimum: {minimum}")
    print(f"Ascending: {result}")
    print(f"Descending: {result2}")
    print(f"Positive count: {positive_count}")
    print(f"Negative count: {negative_count}")
    print(f"Even: {even_count}")
    print(f"Odd: {odd_count}")
