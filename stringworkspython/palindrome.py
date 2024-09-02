# create afunction is_palindrome(word) return true if word is a palindrome string
#else return false


def is_palindrome(word):
    reversed_str=word[::-1]  #reversed_strr="madam"
    return word==reversed_str    #return "madam"=="madam"
print(is_palindrome("malayalam"))


#create a function reverse(word)  return reversed_string
# def reverse(word);   