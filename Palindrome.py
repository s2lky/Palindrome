def is_palindrome(word):
    reversed_word = word[::-1]
    return word == reversed_word

if __name__ == "__main__":
  word = input("Enter a word: ")
  if is_palindrome(word):
    print("The word is a palindrome.")
  else:
    print("The word is not a palindrome.")
