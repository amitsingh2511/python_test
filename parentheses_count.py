# This code calculates the minimum number of additional parentheses '(' or ')' 
# needed to balance the given input string of parentheses. It iterates through the string 
# while keeping track of open parentheses and the count of additional parentheses needed.

# For example, if you input a string like "())(()", the code will tell you how many 
# additional parentheses are needed to make it balanced.

def min_parentheses_to_balance(input_str):
    open_count = 0  # Count of open parentheses '('
    additional_parentheses = 0  # Count of additional parentheses needed to balance

    for char in input_str:
        if char == '(':
            open_count += 1
        elif char == ')' and open_count > 0:
            open_count -= 1
        else:
            additional_parentheses += 1

    additional_parentheses += open_count  # Add remaining open parentheses

    return additional_parentheses

# Input
input_str = input("Enter the string of parentheses: ")

# Calculate and print the result
result = min_parentheses_to_balance(input_str)
print("Minimum additional parentheses needed:", result)
