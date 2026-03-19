"""
Name: Deborah Muchiri AIIM/02945/2024
Date: March 19, 2026
Description: Reverse A String Using two different methods
"""
# String reversal
# Accept user input
user_string = input("Enter your Name: ")

# Method 1: String slicing
def reversed_slicing(text):
    return text[::-1]

# Method 2: Looping through the string
def reversed_loop(text):
    reversed_string = ""
    for character in text:
        reversed_string = character + reversed_string
    return reversed_string

# Method 3: Recursive reversal
def reverse_string_recursive(text):
    if len(text) == 0:
        return text
    else:
        return reverse_string_recursive(text[1:]) + text[0]

# Display the results
def display_result(text):
    print("Method 1 (Slicing): ", reversed_slicing(text))
    print("Method 2 (Loop): ", reversed_loop(text))
    print("Method 3 (Recurve Methods): ", reverse_string_recursive(text))

display_result(user_string)

# Character frequency count
def character_frequency(text, ignore_case=True, ignore_space=False):

    # Handle case Sensitivity
    if ignore_case:
        text = text.lower()
    else:
        text = text.upper()

    # Count frequency
    frequency = {}
    for char in text:
        if ignore_space and char == " ":
            continue

        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    # Display results in formatted table
    print("\nCHARACTER FREQUENCY TABLE")
    print("-" * 30)
    print("Character | Count")
    print("-" * 30)

    # Sort by Character/frequency
    for char, count in sorted(frequency.items()):
        print(f" '{char}'      |    {count}")

    print("-" * 30 )
    print(f"Total unique Characters: {len(frequency)}")

# Handle case sensitive options
character_frequency(user_string, ignore_space=True, ignore_case=False)
