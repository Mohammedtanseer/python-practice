sentence = input("Enter a sentence: ")

# Remove extra spaces at the ends and between words
cleaned = " ".join(sentence.split())

# Case versions
lower_case = cleaned.lower()
upper_case = cleaned.upper()
title_case = cleaned.title()
sentence_case = cleaned.capitalize()

# Counts
char_count = len(cleaned)
char_count_no_spaces = len(cleaned.replace(" ", ""))
word_count = len(cleaned.split())

print("--- Text cleaner ---")
print(f"Original:        '{sentence}'")
print(f"Cleaned:         '{cleaned}'")
print(f"Lower:           {lower_case}")
print(f"Upper:           {upper_case}")
print(f"Title:           {title_case}")
print(f"Sentence case:   {sentence_case}")
print(f"Characters:      {char_count}")
print(f"No-space chars:  {char_count_no_spaces}")
print(f"Words:           {word_count}")




