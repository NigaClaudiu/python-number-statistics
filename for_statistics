numbers = [12, 7, 0, 18, 5, 22, 9, 0, 14, 3]
even_count = 0
odd_count = 0
total_positive = 0
total_negative = 0
average_positive = 0
positive_count = 0

for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
    if numbers[i] > 0:
        total_positive += numbers[i]
        positive_count += 1
    elif numbers[i] < 0:
        total_negative += 1
    else:
        print(f"Zero found at index: {i}")
average_positive = total_positive / positive_count

print(f"Even numbers: {even_count}")
print(f"Odd numbers: {odd_count}")
print(f"Sum of positive numbers: {total_positive}")
print(f"Average of positive numbers: {average_positive}")
