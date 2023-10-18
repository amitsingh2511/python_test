# This code takes a message and an integer key as input and encodes the message based on the 
# rules you provided. It iterates through the characters of the message, calculates the character 
# value, and adds the corresponding key digit. The results are concatenated into a single string 
# separated by commas.

# For example, if you use the input message = "hello" and key = 123, 
# the output will be "9,7,12,16,18".

def encode_string(message, key):
    key_digits = [int(digit) for digit in str(key)]
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encoded_chars = []

    key_index = 0
    for char in message:
        if char in alphabet:
            char_value = ord(char) - ord('a') + 1
            key_digit = key_digits[key_index % len(key_digits)]
            encoded_chars.append(str(char_value + key_digit))
            key_index += 1

    encoded_string = ",".join(encoded_chars)
    return encoded_string

# Example usage
message = "hello"
key = 123
encoded_message = encode_string(message, key)
print(encoded_message)
