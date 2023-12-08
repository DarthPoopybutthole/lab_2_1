print(" *** Digit count and Summation ***")
num = input("Enter an integer: ")

# Counting digits
num_digits = len(num)

# Formatting number with commas
formatted_num = format(int(num), ",")

# Summation of digits
summation = sum(int(digit) for digit in num)

print(f"number = {formatted_num}")
print("Total digits are:", num_digits)
print("Summation =", summation)
