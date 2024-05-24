# First line contains the number of phrases
# Tests whether the phrases are palindromes

import string

amount = int(input())
arr = []
arr1 = []
for i in range(amount):
  phrase = input()
  phrase1 = phrase.lower()
  phrase1 = phrase1.replace(" ", "")
  phrase1 = phrase1.translate(str.maketrans('', '', string.punctuation))
  arr.append(phrase)
  arr1.append(phrase1)

for i in range(len(arr)):
  if arr1[i] == arr1[i][::-1]:
    print("Yes", '"' + arr[i] + '"')
  else:
    print("No", '"' + arr[i] + '"')