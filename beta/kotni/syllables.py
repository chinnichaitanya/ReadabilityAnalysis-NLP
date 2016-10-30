##
#  Count and display the number of syllables in a word.
#

# Read input from the user.
# word = input("Enter a word: ")
# word = word.lower()
word = "incognito"
print(word)

# Count the syllables in the word.
syllables = 0
for i in range(len(word)) :

   # If the first letter in the word is a vowel then it is a syllable.
   if i == 0 and word[i] in "aeiouy" :
      syllables = syllables + 1

   # Else if the previous letter is not a vowel.
   elif word[i - 1] not in "aeiouy" :

      # If it is no the last letter in the word and it is a vowel.
      if i < len(word) - 1 and word[i] in "aeiouy" :
         syllables = syllables + 1

      # Else if it is the last letter and it is a vowel that is not e.
      elif i == len(word) - 1 and word[i] in "aiouy" :
         syllables = syllables + 1

# Adjust syllables from 0 to 1.
if len(word) > 0 and syllables == 0 :
   syllables == 0
   syllables = 1

# Display the result.
print("The word contains", syllables, "syllable(s)")