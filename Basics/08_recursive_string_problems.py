"""
==========================================================
            RECURSIVE STRING PROBLEMS
==========================================================

This program solves the following problems using recursion
only (No loops are used):

1. Reverse a String
2. Count Vowels
3. Count Digits
4. Sum of Digits
5. Count Uppercase Letters
6. Check Palindrome

Author   : Rozy
Language : Python

==========================================================
"""

# --------------------------------------------------------
# Take Input
# --------------------------------------------------------

string = input("Enter a String: ").strip()


# --------------------------------------------------------
# 1. Reverse String
# --------------------------------------------------------

def reverse_string(s):
    # Base Case
    if len(s) <= 1:
        return s

    # Reverse remaining string and place
    # first character at the end.
    return reverse_string(s[1:]) + s[0]


# --------------------------------------------------------
# 2. Count Vowels
# --------------------------------------------------------

def vowel_count(s):
    # Base Case
    if len(s) == 0:
        return 0

    # Count current character if it is a vowel.
    if s[0] in "aeiouAEIOU":
        return 1 + vowel_count(s[1:])

    return vowel_count(s[1:])


# --------------------------------------------------------
# 3. Count Digits
# --------------------------------------------------------

def digit_count(s):
    # Base Case
    if len(s) == 0:
        return 0

    # Count current character if it is a digit.
    if s[0].isdigit():
        return 1 + digit_count(s[1:])

    return digit_count(s[1:])


# --------------------------------------------------------
# 4. Sum of Digits
# --------------------------------------------------------

def sum_digits(s):
    # Base Case
    if len(s) == 0:
        return 0

    # Add current digit if found.
    if s[0].isdigit():
        return int(s[0]) + sum_digits(s[1:])

    return sum_digits(s[1:])


# --------------------------------------------------------
# 5. Count Uppercase Letters
# --------------------------------------------------------

def uppercase_count(s):
    # Base Case
    if len(s) == 0:
        return 0

    # Count uppercase letters.
    if s[0].isupper():
        return 1 + uppercase_count(s[1:])

    return uppercase_count(s[1:])


# --------------------------------------------------------
# 6. Check Palindrome
# --------------------------------------------------------

def palindrome(s):
    # Base Case
    if len(s) <= 1:
        return True

    # Compare the first and last characters.
    # If they match, recursively check the
    # remaining middle substring.
    if s[0].lower() == s[-1].lower():
        return palindrome(s[1:-1])

    return False


# ========================================================
#                     OUTPUT SECTION
# ========================================================

print("\n" + "=" * 50)
print("              RECURSION RESULTS")
print("=" * 50)

print(f"Original String      : {string}")
print(f"Reversed String      : {reverse_string(string)}")
print(f"Total Vowels         : {vowel_count(string)}")
print(f"Total Digits         : {digit_count(string)}")
print(f"Sum of Digits        : {sum_digits(string)}")
print(f"Uppercase Letters    : {uppercase_count(string)}")
print(f"Is Palindrome?       : {palindrome(string)}")

print("=" * 50)
print("\nProgram Executed Successfully!")