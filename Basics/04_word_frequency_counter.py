# ---------------------------------------------------------
# Program 4: Word Frequency Counter
# Concepts Used:
# Strings, Dictionaries, Loops, Functions
# ---------------------------------------------------------

# ---------------------- Input ---------------------- #
sentence = input("Enter a sentence: ").lower()

# -------------------- Functions -------------------- #

# Count total words
def total_words(text):
    words = text.split()
    return len(words)


# Count total characters (including spaces)
def total_characters(text):
    return len(text)


# Count total vowels
def total_vowels(text):
    count = 0

    for char in text:
        if char in "aeiou":
            count += 1

    return count


# Count total consonants
def total_consonants(text):
    count = 0

    for char in text:
        if char.isalpha() and char not in "aeiou":
            count += 1

    return count


# Count frequency of every word
def word_frequency(text):
    words = text.split()
    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency


# -------------------- Main Program -------------------- #

print("\n" + "-" * 55)
print("           WORD FREQUENCY COUNTER PROGRAM")
print("-" * 55)

print(f"\nSentence : {sentence}")

print(f"\nTotal Words       : {total_words(sentence)}")
print(f"Total Characters  : {total_characters(sentence)}")
print(f"Total Vowels      : {total_vowels(sentence)}")
print(f"Total Consonants  : {total_consonants(sentence)}")

print("\nWord Frequency")
print("-" * 20)

frequency = word_frequency(sentence)

for word, count in frequency.items():
    print(f"{word:<15} : {count}")